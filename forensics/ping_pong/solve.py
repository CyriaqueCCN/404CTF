#!/usr/bin/env python3

import pyshark
import binascii

cap = pyshark.FileCapture("ping.pcapng")

i = 0
for p in cap:
    if i % 2 == 0:
        r = binascii.unhexlify(p.icmp.data)
        a = chr(len(r))
        print(a, end="")
    i += 1

