# viết script

- https://hackmd.io/@meowhecker/SJjCsQ3Uh/%2FVYXTfbmMQPqzzhHxMcxQ_g?utm_source=preview-mode&utm_medium=rec

```python=
import argparse #user interface
import subprocess #execute cmd
import sys        #shell
import socket
import textwrap
import threading
import shlex

# use argarse to create the commend interface.

# parser: argument container
parser = argparse.ArgumentParser(
    description="NetCat by meowhecker!!!",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''
    example:
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l #connect to the targetHost
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -c # shell mode
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -u=upload.txt # uploadfile
    netcatMeowhecker.py -t 0.0.0.0 -p 6669 -l -e=~~~# execute commend
    '''))

parser.add_argument("-c", "--commend", action="store_true", help="commend shell")
parser.add_argument("-e", "--execute", help="execute special commend")
parser.add_argument("-l", "--listen", action="store_true", help="listen")
parser.add_argument("-p", "--port", type=int, help="specified port")
parser.add_argument("-t", "--target", help="specified target")
parser.add_argument("-u", "--upload", help="upload the file")
args = parser.parse_args()

def execute(cmd):
    cmd=cmd.strip()
    if not cmd:
        return
    output=subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()


class netCat:
    def __init__(self, args, buffer=None):
        self.args=args
        self.buffer=buffer
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)#setsockopt(level,optionName,value)
        # socket.SQL_SOCKET:　socket is using this option
        # socket.SO_REUEADDR: socket release port instantly

    def run(self):
        if self.args.listen:
            self.listen()
        else:
            self.send()


    def job(self, clientSocket):
        if self.args.execute:
            commend = execute(self.args.execute)
            clientSocket.send(commend.encode())
        elif self.args.upload:
            fileBuffer=b''

            while True:
                fileData = clientSocket.recv(4096)
                if fileData:
                    fileBuffer += fileData
                else:
                    break
            with open(self.args.upload,"wb") as fileupload:
                fileupload.write(fileBuffer)
            message = f'file save{self.args.upload}'
            clientSocket.send(message.encode())

        elif self.args.commend:
            commendBuffer=b''
            #print("meow")
            while True:
                try:
                    clientSocket.send(b'Meowhecker#>')
                    while '\n' not in commendBuffer.decode():
                        commendBuffer += clientSocket.recv(64)
                    response = execute(commendBuffer.decode())
                    if response:
                        clientSocket.send(response.encode())
                    commendBuffer=b''
                except Exception as e:
                    print(f'sever killed {e}')
                    self.socket.close
                    sys.exit()
    def listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)
        print(f'listening on {self.args.target}:{self.args.port}')
        while 1:
            clientSocket, address= self.socket.accept()
            print(f'connection from {address[0]}:{address[1]}')
            thread = threading.Thread(target=self.job, args=(clientSocket,))
            thread.start()

    def send(self):
        #print("meow2")
        self.socket.connect((self.args.target,self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:
            receiveLen = 1
            response=''
            while receiveLen:
                message = self.socket.recv(4096)
                receiveLen = len(message)
                response += message.decode
                if receiveLen < 2:
                    break

                if response:
                    print(response)
                    buffer=input('MeowheckerShellResponse:#>')
                    buffer+='\n'
                    self.socket.send(buffer.encode())

        except KeyboardInterrupt:
            print("Netcat terminated")
            self.socket.close()
            sys.exit()

if __name__ =="__main__":
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
    nc =netCat(args,buffer.encode)
    nc.run()

```

- https://hackmd.io/@meowhecker/SJjCsQ3Uh/%2FV8KvxlroQy2ZuLOP0a1SZA?utm_source=preview-mode&utm_medium=rec

## Scapy

- https://viblo.asia/p/xay-dung-scan-port-voi-python-va-thu-vien-scapy-MkNLrZyWLgA
- https://hackmd.io/@JohnathanHuuTri/rkdzitQtn?utm_source=preview-mode&utm_medium=rec
- https://hackmd.io/@0xff07/HJHmbPKmo#%E8%A8%88%E7%AE%97%E6%A9%9F%E7%B6%B2%E8%B7%AF---Scapy
- https://scapy.net/talks/scapy_pacsec05.pdf

`echo 1 > /pro/sys/net/ipv4/ip_forward`

- https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_attacks/arp_spoofing/index.html
- https://www.cit.ctu.edu.vn/~dtnghi/nid/scapy.pdf
- https://anonyviet.com/pyhack-bai-3-network-scanner-quet-thong-tin-mang/
- https://wifipentesting.blogspot.com/2016/12/su-dung-scapy.html
- https://whitehat.vn/threads/dos-voi-scapy.583/

- https://guyinatuxedo.github.io/01-intro_assembly/assembly/index.html

## Phân tích Pcap online

- https://apackets.com/

## tạo thành công một gói request ARP

- https://anonyviet.com/pyhack-bai-3-network-scanner-quet-thong-tin-mang/

## Chèn code vào packet

- https://tek4.vn/cach-inject-code-vao-http-response-trong-mang-bang-python
- https://hackmd.io/@JohnathanHuuTri/rkdzitQtn?utm_source=preview-mode&utm_medium=rec
- https://thepythoncode.com/article/building-arp-spoofer-using-scapy

## DHCP

- https://tek4.vn/tao-trinh-lang-nghe-dhcp-su-dung-scapy-trong-python

```python!
from scapy.all import *
import time


def listen_dhcp():
    # Make sure it is DHCP with the filter options
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)')


def print_packet(packet):
    # initialize these variables to None at first
    target_mac, requested_ip, hostname, vendor_id = [None] * 4
    # get the MAC address of the requester
    if packet.haslayer(Ether):
        target_mac = packet.getlayer(Ether).src
    # get the DHCP options
    dhcp_options = packet[DHCP].options
    for item in dhcp_options:
        try:
            label, value = item
        except ValueError:
            continue
        if label == 'requested_addr':
            # get the requested IP
            requested_ip = value
        elif label == 'hostname':
            # get the hostname of the device
            hostname = value.decode()
        elif label == 'vendor_class_id':
            # get the vendor ID
            vendor_id = value.decode()
    if target_mac and vendor_id and hostname and requested_ip:
        # if all variables are not None, print the device details
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")


if __name__ == "__main__":
    listen_dhcp()


```

- https://aptech.vn/kien-thuc-tin-hoc/bao-ve-may-chu-bang-scapy-phan-1.html

## Scan nmap

- https://viblo.asia/p/nmap-port-scan-cac-phuong-phap-quet-cong-tu-co-ban-den-nang-cao-gDVK2PMwlLj

chỉnh port forwarding trên window

![image](https://hackmd.io/_uploads/By7dFPECa.png)

![image](https://hackmd.io/_uploads/SynrcPV06.png)

- https://www.youtube.com/watch?v=3fFMsjB-068

https://www.youtube.com/watch?v=SDCKXGMgcgA&t=140s

- https://hackmd.io/@ephemeral-instance/HJc4Xxc-O
