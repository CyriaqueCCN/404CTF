from scapy.all import *

packets = rdpcap("ping.pcapng")


res = ""
for p in packets:
    #res += p.data
    print(p)
