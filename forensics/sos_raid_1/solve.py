#!/usr/bin/env python3

from pwn import *

D0 = "disk0.img"
D1 = "disk1.img"
D2 = "disk2.img"
DR = "original.img"

CHUNK_SIZE = 1
DISK_SIZE = 27756

# RAID-5 needs at least 3 disks to operate
# we have disk0 and disk1, stands to reason we need to get back disk2

# recreate missing disk2
def fxor():
    with open(D0, "rb") as d0:
        with open(D1, "rb") as d1:
            with open(D2, "wb") as d2:
                x = d0.read()
                y = d1.read()
                d2.write(xor(x, y))

# recreate original disk
# i % 3 == 0 : parity on D2
# i % 3 == 1 : parity on D1
# i % 3 == 2 : parity on D0
def regen():
    with open(D0, "rb") as d0:
        with open(D1, "rb") as d1:
            with open(D2, "rb") as d2:
                with open(DR, "wb") as rd:
                    x = 2
                    for i in range(DISK_SIZE):
                        if i % 3 != 2:
                            rd.write(d0.read(CHUNK_SIZE))
                        if i % 3 != 1:
                            rd.write(d1.read(CHUNK_SIZE))
                        if i % 3 != 0:
                            rd.write(d2.read(CHUNK_SIZE))
fxor()
regen()
