#!/usr/bin/env python3

FN = "group8.txt"

with open(FN, "r") as f:
    r = f.read().strip().split()

for b in r:
    x = int(b[::-1][1:7], 2)
    print(chr(x), end="")
