# Thực hành Switch CCNA bypass login

- đầu tiên để kết nối với switch tại phòng server mình kết nối qua đường dây Serial thông qua công cụ Putty

![image](https://hackmd.io/_uploads/B1JYRnc0p.png)

- để có thể kết nối với connection type là Serial mình cần biết máy tính của mình sẽ kết nối qua cổng COM bao nhiêu
  - mình vào device manager thấy được port kết nối ở đây là COM4

![image](https://hackmd.io/_uploads/SJWS0hqCT.png)

- kết nối và mình vào được giao diện CLI tương tác với switch

chúng ta biết thiết bị switch của cisco phải trải qua 5 bước để boot

- bước 1: Switch sẽ load chương trình power-on self-test (POST) được lưu trữ trong ROM. POST sẽ check các hệ thống con CPU. Nó test CPU, DRAM và flash để đọc các file hệ thống trong flash
- bước 2: Switch sẽ tải phần mềm boot loader đó là 1 chương trình nhỏ được lưu ROM để chạy ngay sau POST chạy kiểm tra thành công
- bước 3: khởi tạo các thanh ghi CPU
- bước 4: boot loader khởi tạo hệ thống file hệ thống
- bước 5: boot loader load IOS những file image mặc định vào bộ nhớ và điều khiển switch bằng IOS

file start-up config được gọi là config.text và được lưu ở trong flash

- vì chúng ta không biết được mật khẩu để vào các chế độ đặc quyền của switch đang chạy
- nên mình sẽ thực hiện bypass những mật khẩu này bằng cách khởi động lại switch và nhấn liên tục vào nút mode để vào chế độ tương tác với boot loader **switch:** sau đó đổi tên file **config.text**
- sau đó boot lại switch khi đó switch sẽ không tìm thấy file **config.text** và sẽ trở về cấu hinh ban đầu và chúng ta có thể vào các chế độ đặc quyền để cấu hình

![image](https://hackmd.io/_uploads/ByXBmQiRp.png)

![image](https://hackmd.io/_uploads/HyApM3sCa.png)

- tiến hành khởi động switch bằng cách rút dây nguồn và cắm lại
- sau đó mình nhấn giữ nút **MODE** liên tục trong khoảng 15 giây cho đến khi đèn chuyển sang màu xanh

![image](https://hackmd.io/_uploads/HySyTGjCT.png)

- sau đó mình vào được chế độ tương tác với boot loader **switch:**
- mình liệt kê các file và thư mục với lệnh **dir**

![image](https://hackmd.io/_uploads/HkYWkp5CT.png)

- tiếp theo mình khởi tạo hệ thống tập tin flash bằng lệnh **flash_init**
  - và lúc này mình có thể liệt kê các file trong flash

![image](https://hackmd.io/_uploads/rkzSxp906.png)

- trong flash chúng ta thấy file **config.text** là file cấu hình switch sẽ đọc khi khởi động lên vậy chúng ta cần xóa hoặc đổi tên file này để cấu hình trắng và switch sẽ về mặc định khi chưa cấu hình

![image](https://hackmd.io/_uploads/rJkK-6qRT.png)

![image](https://hackmd.io/_uploads/HJa8W6cCp.png)

- mình đã đổi tên file **config.text** trong flash thành **config.xyz**
  - và lúc này chúng ta chỉ cần khởi động lại switch với lệnh **boot**

![image](https://hackmd.io/_uploads/HkDcb65CT.png)

![image](https://hackmd.io/_uploads/ByE6-a50p.png)

![image](https://hackmd.io/_uploads/H1a6b6qAT.png)

![image](https://hackmd.io/_uploads/HyVAZTc0T.png)

![image](https://hackmd.io/_uploads/SJ1lfac06.png)

- và mình đã vào được user mode

![image](https://hackmd.io/_uploads/H1wMfTqC6.png)

- lúc này chúng ta có thể vào rename lại file config.xyz về config.text để cấu hình lúc trước không mất bằng lệnh **rename flash:config.text.old flash:config.text** và Copy file cấu hình vào RAM và đổi lại password mới

  - nhưng mình đã cấu hình mới lại từ đầu

- đầu tiên là đặt mật khẩu cho dây console là cisco

![image](https://hackmd.io/_uploads/rkrOMT9Cp.png)

- tiếp theo mình đặt banner motd

![image](https://hackmd.io/_uploads/SyVAG65AT.png)

- đặt hostname
- đặt mật khẩu cho các đường vty để mình có thể ssh đến

![image](https://hackmd.io/_uploads/r1NbXa5Cp.png)

- tiếp theo mình cấu hình SSH với các bước sau:
  1. với bước đầu tiên mình đặt domain name là cisco.com
  2. chọn ssh version là 2
  3. tạo user mới để ssh với username là admin và password là admin
  4. chọn phương thức mã hóa ssh là RSA
  5. và mình chọn số bit được dùng để tạo khóa là 1024

![image](https://hackmd.io/_uploads/ryFhXp5Ra.png)

- tiếp theo mình vào các đường vty đặt đăng nhập bằng khóa RSA vừa tạo ở local

![image](https://hackmd.io/_uploads/BJ0k4pc0p.png)

- mình vào đặt địa chỉ IP cho vlan1 trên switch để có thể SSH đến - do chúng ta không biết chính xác mạng hiện tạo đang dùng tại phòng server - nên mình sẽ dùng DHCP để cấp địa chỉ IP động cho Vlan1 này
  ![image](https://hackmd.io/_uploads/r15gLpcCT.png)
- lưu lại các cấu hình vừa rồi và mình thấy file config.text mới được tạo trong flash

![image](https://hackmd.io/_uploads/ByUaVa5Rp.png)

![image](https://hackmd.io/_uploads/rJ8E4pqRT.png)

- mình kiểm tra lại các câu lệnh vừa cấu hình với **show running-config**

![image](https://hackmd.io/_uploads/SkgQS690a.png)

![image](https://hackmd.io/_uploads/H1F7HaqAT.png)

thoát ra thấy banner motd đã được đặt

![image](https://hackmd.io/_uploads/H1FMIa50T.png)

- mình vào xem địa chỉ IP được DHCP được cấp cho switch và được **192.168.192.79**

![image](https://hackmd.io/_uploads/rJoUU6cAT.png)

- sau đó chúng ta sẽ SSH lại switch này qua Putty

![image](https://hackmd.io/_uploads/HkXTLT9CT.png)

- và mình đăng nhập với username là admin và password là admin mà chúng ta vừa cấu hình

![image](https://hackmd.io/_uploads/HyTAUT5Ra.png)

- và mình có thể vào cấu hình switch này từ xa

![image](https://hackmd.io/_uploads/Sy6bwpqAT.png)

![image](https://hackmd.io/_uploads/H1jMwa9Aa.png)

![image](https://hackmd.io/_uploads/S1VW-piR6.png)

![image](https://hackmd.io/_uploads/SJ9uzpjAp.png)

![image](https://hackmd.io/_uploads/r1jrZpsAa.png)
