# IP Spoofing

![image](https://hackmd.io/_uploads/SkP4pd5Ca.png)

## Khái niệm & Khai thác & Phòng tránh

### Khái niệm

- **Internet Protocol (IP) spoofing** (Giả mạo địa chỉ IP) là loại tấn công độc hại nhằm che dấu các gói IP nguồn để khó phát hiện chúng nằm ở đâu. Những người tấn công mạng sẽ tạo ra các gói tin và thay đổi địa chỉ IP nguồn. Từ đó mạo danh một hệ thống máy tính hoặc có thể ngụy tạo danh tính của người gửi.
- Trong IP spoofing tin tặc sẽ thay đổi địa chỉ IP nguồn trong tiêu đề gói gửi đi. Từ đó khiến máy tính đích xem gói tin đến từ một nguồn đáng tin cậy. Họ dùng các công cụ để tạo ra các tiêu đề gói tin giả bằng cách làm sai lệch và liên tục lấy ngẫu nhiên địa chỉ nguồn. Ngoài ra, cũng có thể sử dụng địa chỉ IP của thiết bị khác có sẵn để thay thế.

- các trường trong IPv4

![image](https://hackmd.io/_uploads/S1wUducRp.png)

![image](https://hackmd.io/_uploads/SJmvducAp.png)

- các trường trong IPv6

![image](https://hackmd.io/_uploads/HJ0AddqCp.png)

![image](https://hackmd.io/_uploads/SyCJY_90T.png)

Mạng máy tính giao tiếp thông qua các gói dữ liệu. Mỗi gói này chứa nhiều header, một trong số đó được gọi là "Source IP Address", chứa thông tin IP của đối tượng gửi.

- Các mạng máy tính giao tiếp với nhau thông qua việc trao đổi các gói dữ liệu mạng (network packet). Trong đó, mỗi packet chứa nhiều header dùng dể định tuyến và đảm bảo tính liên tục của kết nối. Mỗi header như vậy có chứa ‘Source IP Address’ (IP nguồn), cho biết địa chỉ của người gửi các packet.

Giả mạo IP là hành vi sửa đổi nội dung Source IP header với các số ngẫu nhiên, nhằm che dấu danh tính, mạo danh hệ thống khác, hoặc khởi tạo một cuộc tấn công.

Thông qua giả mạo IP, kẻ tấn công có thể chuyển hướng phản hồi, dễ dàng đánh cắp và sử dụng dữ liệu người dùng, làm quá tải hoặc gián đoạn server, ngoài ra còn có thể lây nhiễm các phần mềm độc hại.

Kẻ tấn công thường giả mạo nhiều Source IP ngẫu nhiên để gây khó khăn khó khăn cho việc ngăn chặn các cuộc tấn công vì gây hiểu lầm rằng chúng xuất phát từ nhiều nguồn.

#### Các hình thức giả mạo IP

Hai cuộc tấn công tiêu biểu có thể được khởi tạo thông qua giả mạo IP:

- **Masking botnet**: IP spoofing attack có thể dùng để giành quyền truy cập vào các máy tính thông qua việc masking các botnet. Trong đó, botnet là một nhóm các máy tính được kết nối vối nhau, thực hiện những tác vụ lặp đi lặp lại để giữ cho website hoạt động. Các cuộc tấn công IP spoofing sẽ mask những botnet này, rồi sử dụng kết nối của chúng để đạt được mục đích tấn công. Chẳng hạn như flooding hoặc crash các website, server, mạng bằng data. Bên cạnh đó là liên tục spam và gửi nhiều malware khác đến nạn nhân.
- **Tấn công DDoS** là hành vi nhằm làm chậm hoặc sập server. Khả năng giả mạo IP của các gói tin là một lỗ hổng bị nhiều cuộc tấn công DDoS khai thác. Để giữ cho cuộc tấn DoS hoặc DDoS không bị phát hiện, giả mạo IP thường được sử dụng để ngụy trang nguồn gốc của các cuộc tấn công và gây khó khăn cho việc truy tìm nguồn gốc và ngăn chặn chúng.
- **Tấn công MITM** chặn các gói tin được gửi giữa các các hệ thống, thay đổi các gói và sau đó gửi chúng đến đích đã định, hệ thống gửi và nhận không biết rằng liên lạc của chúng đã bị giả mạo mà vẫn tiếp tục, trong khi quá trình truyền bị nghe trộm toàn bộ. Theo thời gian, kẻ tấn công thu thập vô số thông tin nhạy cảm mà họ có thể sử dụng để đánh cắp danh tính hoặc bán.
  - Truyền dữ liệu trên Internet được tạo thành từ nhiều gói dữ liệu và mỗi gói chứa nhiều IP header, header chia sẻ thông tin định tuyến về gói tin, bao gồm Source IP và Destination IP. Source IP có thể được thay bằng IP giả mạo. Kẻ tấn công thực hiện hành vi này bằng cách chặn một gói tin và sửa đổi trước khi gửi đi. Điều này làm cho IP có vẻ như từ một nguồn đáng tin cậy nhưng thực tế đang che dấu IP của một bên thứ ba không xác định.

![image](https://hackmd.io/_uploads/H1e5Y_5Aa.png)

Kẻ tấn công có thể dễ dàng phát hiện ra việc hệ thống chỉ dùng IP để xác thực và vượt qua chúng một cách đơn giản với giả mạo IP, việc sử dụng xác thực đơn giản như vậy cần được thay thế bằng các phương pháp mạnh mẽ hơn, như xác thực nhiều bước.

#### Một số dấu hiệu đáng ngờ có thể cho thấy có IP spoofing đang diễn ra:

- Các gói tin đến từ các địa chỉ IP không xác định.
- Các gói tin có địa chỉ IP nguồn và đích không khớp.
- Các gói tin có số lượng lớn hoặc tần suất cao bất thường.
- Các gói tin có chứa dữ liệu đáng ngờ hoặc độc hại.

### Khai thác

Để thực hiện giả mạo IP, những kẻ đánh cắp thông tin cần thực hiện một số bước như sau:

- Cần tìm một địa chỉ IP đáng tin cậy mà thiết bị nhận cho phép tham gia vào mạng.
- Có khả năng chặn gói tin và hoán đổi tiêu đề IP thực. Cần có công cụ dò tìm mạng hoặc sử dụng giao thức phân giải địa chỉ ARP để chặn các gói trên mạng và thu thập địa chỉ IP để giả mạo.

Sau khi có được địa chỉ IP đáng tin cậy, kẻ tấn công cần có khả năng chặn gói tin và hoán đổi tiêu đề IP thực. Điều này có thể được thực hiện bằng phần mềm hoặc phần cứng chuyên dụng.

Khi kẻ tấn công đã có địa chỉ IP đáng tin cậy và khả năng chặn gói tin, họ có thể bắt đầu gửi các gói dữ liệu IP giả mạo đến thiết bị đích. Các gói dữ liệu này sẽ được thiết bị đích xử lý như thể chúng đến từ một nguồn đáng tin cậy.

#### IP spoofing trong tấn công lớp ứng dụng (Application layer)

![image](https://hackmd.io/_uploads/H1ae_tcRT.png)

Để có thể thiết lập được kết nối lớp ứng dụng, host và khách truy cập cần phải tham gia vào quá trình xác minh lẫn nhau, còn gọi là TCP three-way handshake.

Quá trình bao gồm việc trao đổi các packet SYN và ACK như sau:

1. Người truy cập gửi một SYN packet đến host.
2. Host phản hồi bằng một SYN – ACK.
3. Tiếp đến, khách truy cập xác nhận thông qua phản hồi bằng một ACK packet.

IP spoofing nguồn sẽ can thiệp vào bước thứ 3 của quá tình trên. Cụ thể, nó sẽ ngăn khách truy cập nhận lại SYN-ACK, thay vào đó sẽ gửi nó đến địa chỉ IP giả mạo.

Tất cả các cuộc tấn công vào lớp ứng dụng đều dựa vào các kết nối TCP và việc đóng vòng lặp 3-way handshake. Do đó, chỉ những cuộc tấn công DDoS ở lớp mạng mới có thể sử dụng các địa chỉ giả mạo.

### Phòng tránh

Nhà phát triển:

- Các nhà phát triển web được khuyến khích chuyển các trang web sang IPv6. Nó giúp việc giả mạo IP khó hơn bằng cách bao gồm các bước mã hóa và xác thực
- Tạo các danh sách kiểm soát truy cập địa chỉ IP.
- hệ thống lọc gói để phân tích lưu lượng mạng tại các điểm cuối. Hệ thống này thường được tích hợp trong bộ định tuyến và tường lửa, có hai loại chính: lọc gói vào và lọc gói ra.
  - Lọc gói vào (Ingress Filtering) kiểm tra các gói dữ liệu đến để xác minh xem địa chỉ IP nguồn có khớp với địa chỉ IP đáng tin cậy hay không. Bất kỳ gói dữ liệu nào không khớp sẽ bị từ chối.
  - Lọc gói ra (Egress Filtering) kiểm tra các gói dữ liệu đi để xác minh xem địa chỉ IP nguồn có khớp với địa chỉ mạng của tổ chức hay không. Điều này giúp ngăn chặn các cuộc tấn công IP spoofing.
- Giám sát lưu lượng mạng: Điều này có thể giúp bạn phát hiện các hoạt động đáng ngờ, chẳng hạn như các gói tin đến từ các địa chỉ IP không xác định.
- Sử dụng hệ thống phát hiện xâm nhập (IDS): IDS có thể giúp phát hiện các cuộc tấn công mạng, bao gồm cả IP spoofing. IDS có thể được cấu hình để gửi cảnh báo khi phát hiện các hoạt động đáng ngờ.
- Sử dụng các công cụ phân tích dữ liệu: Các công cụ phân tích dữ liệu có thể giúp bạn phân tích lưu lượng mạng và phát hiện các dấu hiệu của IP spoofing.
- Sử dụng giao thức mã hóa

Người dùng cuối:

- Việc phát hiện giả mạo IP là gần như không thể. Tuy nhiên, có thể giảm thiểu nguy cơ bị các loại giả mạo bằng cách sử dụng các giao thức mã hóa an toàn như HTTPS và đảm bảo rằng biểu tượng ổ khóa luôn xuất hiện trước URL truy cập.
- Tránh lướt web trên WiFi công cộng, không có mật khẩu. Bảo mật mạng WiFi gia đình bằng cách cập nhật tên người dùng và mật khẩu mặc định trên bộ định tuyến bằng một mật khẩu mạnh.

## IP Spoofing Lab

Chúng ta sẽ thực hiện tạo một chương trình Giả mạo IP đơn giản. Chúng ta sẽ gửi gói ICMP-Echo-Request, thường được gọi là ping, đến máy chủ từ xa sử dụng địa chỉ IP nguồn đã bị cố tình làm sai lệch.

```python
# Import the neccasary modules.
import sys
from scapy.all import sr, IP, ICMP
from faker import Faker
from colorama import Fore, init

# Initialize colorama for colored console output.
init()
# Create a Faker object for generating fake data.
fake = Faker()

# Function to generate a fake IPv4 address.
def generate_fake_ip():
    return fake.ipv4()

# Function to craft and send an ICMP packet.
def craft_and_send_packet(source_ip, destination_ip):
    # Craft an ICMP packet with the specified source and destination IP.
    packet = IP(src=source_ip, dst=destination_ip) / ICMP()
    # Send and receive the packet with a timeout.
    answers, _ = sr(packet, verbose=0, timeout=5)
    return answers

# Function to display a summary of the sent and received packets.
def display_packet_summary(sent, received):
    print(f"{Fore.GREEN}[+] Sent Packet: {sent.summary()}\n")
    print(f"{Fore.MAGENTA}[+] Response: {received.summary()}")

# Check if the correct number of command-line arguments is provided.
if len(sys.argv) != 2:
    print(f"{Fore.RED}[-] Error! {Fore.GREEN} Please run as: {sys.argv[0]} <dst_ip>")
    sys.exit(1)

# Retrieve the destination IP from the command-line arguments.
destination_ip = sys.argv[1]
# Generate a fake source IP.
source_ip = generate_fake_ip()
# Craft and send the packet, and receive the response.
answers = craft_and_send_packet(source_ip, destination_ip)
# Display the packet summary for each sent and received pair.
for sent, received in answers:
    display_packet_summary(sent, received)
```

đoạn code sẽ :

- Import các module cần thiết:
  - sys: Cung cấp truy cập đến các biến và chức năng liên quan đến hệ thống.
  - sr, IP, ICMP từ scapy.all: Scapy là một thư viện Python mạnh mẽ cho việc tạo, gửi và nhận các gói tin mạng.
  - Faker từ faker: Thư viện Faker được sử dụng để tạo dữ liệu giả mạo như địa chỉ IP.
- Fore, init từ colorama: Colorama là một công cụ giúp thêm màu sắc vào console output.
- Khởi tạo colorama để tạo ra console output có màu sắc.
- Tạo một đối tượng Faker để sinh dữ liệu giả mạo.
- Định nghĩa hàm generate_fake_ip() để sinh một địa chỉ IPv4 giả mạo.
- Định nghĩa hàm craft_and_send_packet() để tạo và gửi một gói tin ICMP từ một địa chỉ IP nguồn đến một địa chỉ IP đích.
- Định nghĩa hàm display_packet_summary() để hiển thị tóm tắt về gói tin đã gửi và phản hồi nhận được.
- Kiểm tra xem số lượng đối số dòng lệnh đã được cung cấp đúng không. Nếu không, hiển thị thông báo lỗi và thoát.
- Lấy địa chỉ IP đích từ đối số dòng lệnh.
- Sinh một địa chỉ IP nguồn giả mạo.
- Tạo và gửi gói tin, sau đó nhận phản hồi.
- Hiển thị tóm tắt về mỗi cặp gói tin đã gửi và nhận được.

địa chỉ ip của máy kali attacker là `192.168.255.128`

![image](https://hackmd.io/_uploads/ryxy6YqRp.png)

địa chỉ của máy ubuntu victim là `192.168.255.129`

![image](https://hackmd.io/_uploads/Hya0W5q0p.png)

Lưu ý rằng mỗi lần chúng ta chạy chương trình, các IP khác nhau sẽ được chỉ định làm IP nguồn. Ngoài ra, máy mục tiêu (có thể khai thác được) sẽ phản hồi IP nguồn. Vì vậy, trong tình huống thực tế, nếu chúng ta có hành vi độc hại, chúng tôi sẽ không thể bị theo dõi phần nào vì máy mục tiêu nhìn thấy IP nguồn không thuộc về chúng ta (ngay cả khi đó là chúng ta). Đây là những gì kẻ tấn công làm khi thực hiện các cuộc tấn công như DoS và MITM.

- tiến hành tấn công và mình chạy file ip_spoofer.py ở trên và đền ip của victim là `192.168.255.129`

![image](https://hackmd.io/_uploads/S1zsW59A6.png)

- tấn công thành công khi mỗi lần chạy file này mình lại được nguồn gửi là 1 địa chỉ IP khác

## Tham khảo

- https://thepythoncode.com/article/make-an-ip-spoofer-in-python-using-scapy#google_vignette
