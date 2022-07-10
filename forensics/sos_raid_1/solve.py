#!/usr/bin/env python3

from itertools import permutations

D0 = "disk0.img"
D1 = "disk1.img"
D2 = "disk2.img"

DISK_SIZE = 27756

# RAID-5 needs at least 3 disks to operate
# we have disk0 and disk1, stands to reason we need to get back disk2

def bxor(s1, s2):
    return bytes(a ^ b for a, b in zip(s1, s2))

def recreate_disk_2():
    with open(D0, "rb") as d0:
        with open(D1, "rb") as d1:
            with open(D2, "wb") as d2:
                x = d0.read()
                y = d1.read()
                d2.write(bxor(x, y))
                print("Disk 2 regenerated")

# recreate original disk
# i % 3 == 0 : parity on D2
# i % 3 == 1 : parity on D1
# i % 3 == 2 : parity on D0
# perm [2, 0, 1]
def regen(p):
    pfname = "res_" + "".join(map(str, p)) + ".img"
    z = [0, 0, 0]
    with open(D0, "rb") as d0:
        with open(D1, "rb") as d1:
            with open(D2, "rb") as d2:
                with open(pfname, "wb") as rd:
                    z[p[0]] = d0.read()
                    z[p[1]] = d1.read()
                    z[p[2]] = d2.read()
                    for i in range(DISK_SIZE):
                        if i % 3 != 2:
                            rd.write(z[0][i:i+1])
                        if i % 3 != 1:
                            rd.write(z[1][i:i+1])
                        if i % 3 != 0:
                            rd.write(z[2][i:i+1])
                    print(f"{pfname} generated")

def main():
    recreate_disk_2()
    perms = permutations([0, 1, 2])
    for p in perms:
        regen(p)

main()
