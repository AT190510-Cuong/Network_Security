#!/usr/bin/python3
from scapy import *

num_packets = 0
def print_pkt(pkt):
    print_pkt.num_packets += 1
    print("\n=======================packet{}=======================".format(num_packets))
    pkt.show()

print_pkt.num_packets = 0
pkt = sniff(iface='eth0', filter='icmp', prn=print_pkt)