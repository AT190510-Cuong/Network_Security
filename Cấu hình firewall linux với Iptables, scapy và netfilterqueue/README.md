# Cấu hình firewall linux với Iptables, scapy và netfilterqueue

- thư viện netfilterqueue là một thư viện cho phép tương tác với các gói tin được gửi đến và gửi đi qua các rules của iptables.

lab này mình dùng máy window 10 cùng với máy ảo kali linux 

chúng ta dùng đoạn code sau để firewall filter và sửa gói tin 
- mong muốn của ta là nếu client kết nối tới server và gửi dòng chữ ```flag``` thì script sẽ thay dòng chữ đó thành ```Helo``` và tiếp tục gửi tới server (lưu ý nhớ giữ nguyên độ dài của load)

```python
from scapy.all import *
from netfilterqueue import NetfilterQueue
import os

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    print("================================start action===========================")
    if scapy_packet.haslayer(TCP) and scapy_packet.haslayer(Raw):
        scapy_packet = modify_packet(scapy_packet)
    packet.set_payload(bytes(scapy_packet))
    packet.accept()

def modify_packet(scapy_packet):
    scapy_packet[Raw].load = scapy_packet[Raw].load.replace(b'flag', b'Helo')
    del scapy_packet[IP].len
    del scapy_packet[IP].chksum
    del scapy_packet[TCP].chksum
    return scapy_packet

if __name__=='__main__':
    try:
        if os.geteuid() != 0:
            exit("Run with root permission!")
        os.system('iptables -A INPUT -j NFQUEUE --queue-num 0')
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system('iptables -D INPUT -j NFQUEUE --queue-num 0')
```
- Hàm process_packet(packet): Đây là hàm chính được sử dụng để xử lý mỗi gói tin được gửi đến qua NetfilterQueue. Trong hàm này, gói tin được chuyển đổi thành một đối tượng Scapy để dễ dàng xử lý. Sau đó, gói tin được kiểm tra xem có chứa lớp TCP và Raw không. Nếu có, gói tin sẽ được sửa đổi bằng cách gọi hàm modify_packet, sau đó gói tin sẽ được chuyển đổi lại thành dữ liệu byte và được chấp nhận (accept).
- Hàm modify_packet(scapy_packet): Hàm này nhận đầu vào là một đối tượng gói tin Scapy và thực hiện việc sửa đổi dữ liệu gói tin. Trong ví dụ này, nội dung của lớp Raw được thay thế các chuỗi 'flag' thành 'Helo'. Sau đó, các trường dữ liệu checksum của IP và TCP được xóa bỏ để Scapy có thể tự động tính toán lại.
- Phần chính của chương trình được kiểm tra thông qua if __name__ == '__main__': Trong phần này, chương trình kiểm tra xem nó có được chạy với quyền root không. Sau đó, nó thiết lập một quy tắc iptables để chuyển hết các gói tin đến một hàng đợi NetfilterQueue. Tiếp theo, nó tạo một đối tượng NetfilterQueue và ràng buộc nó với hàm process_packet. Cuối cùng, chương trình chạy vòng lặp vô hạn để xử lý các gói tin đến qua hàng đợi, và nếu người dùng nhấn Ctrl+C, nó sẽ gỡ bỏ quy tắc iptables.


chạy file trên và mình tạo 1 server để netcat đến ở port 8000 và cho máy window kết nối đến và truyền tin
- khi client gửi dòng chữ flag, server sẽ nhận được chữ Helo:


![image](https://hackmd.io/_uploads/HJ4wCpHRa.png)

sau khi kết thúc chương trình với Ctrl + C  rule mới thêm ở INPUT đã được loại bỏ 

![image](https://hackmd.io/_uploads/ryH1Q0HAT.png)

- các chữ khác với **flag** sẽ không bị chuyển đổi 

![image](https://hackmd.io/_uploads/ryec-RrAT.png)

làm lại và mình bắt được các packets netcat trên wireshark
- filter tcp và địa chỉ ip của máy window 

![image](https://hackmd.io/_uploads/Skp-xRHRp.png)

- mình được các gói tin chứa thông tin trước khi vào netfilterqueue

![image](https://hackmd.io/_uploads/rJxSg0B0p.png)


