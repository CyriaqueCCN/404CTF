#!/usr/bin/env python3

FN = "group8.txt"

with open(FN, "r") as f:
    r = f.read().strip().split()

res = b""
for b in r:
    #x = int(b[::-1][1:7], 2)
    #print(chr(x), end="")
    x = int(b, 2).to_bytes(1, "little")
    res += x

with open("tobytes.txt", "wb") as fr:
    fr.write(res)
#print(res)
