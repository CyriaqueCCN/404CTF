#!/usr/bin/env python3

import pyshark
import base64
import binascii

cap = pyshark.FileCapture("ping.pcapng")

r = b""
i = 0
for p in cap:
    if i % 2 == 0:
        print(p.icmp.data)
        r += binascii.unhexlify(p.icmp.data)
    i += 1

with open("total", "wb") as f:
    f.write(r)

#print(r)
