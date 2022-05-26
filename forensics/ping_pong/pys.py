import pyshark
import base64

cap = pyshark.FileCapture("ping.pcapng")

r = []
i = 0
for p in cap:
    if i % 2 == 0:
        r.append(p.icmp.data)
    i += 1

print(r)
