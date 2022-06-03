#!/usr/bin/env python3

import pyshark as ps

FNAME = "extracted"
CNAME = "ransomware1.pcapng"
VICT_IP = "172.17.0.1"

def get_packets(cap):
    res = b""
    with open(FNAME, "wb") as r:
        for p in cap:
            if "TCP" in p and p.ip.src == VICT_IP:
                res += int(p.tcp.flags, 16).to_bytes(1, byteorder="little")
        r.write(res)

def main():
    cap = ps.FileCapture(CNAME)
    pkts = get_packets(cap)

main()
