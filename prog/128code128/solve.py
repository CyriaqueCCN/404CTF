#!/usr/bin/env python3

from PIL import Image
from base64 import b64decode
from io import BytesIO
from pwn import remote

CODE_DEFAULT = "ascii"
CRC_PRESENT = False

def create_mapping():
    f = open("mappings.tsv", "r")
    lines = f.readlines()
    f.close()
    code = {}
    for l in lines:
        r = l.split('\t')
        idx = r[7].strip()
        asc = r[5].strip()
        if len(asc) < 4 and "—" not in asc:
            asc = chr(int(asc))
        code[idx] = {
            "a"     : r[2].strip(),
            "b"     : r[3].strip(),
            "c"     : r[4].strip(),
            "val"   : r[0].strip(),
            "hex"   : r[1].strip(),
            "ascii" : asc,
            "latin1": r[6].strip()
        }
    return code

def get_char(b, code):
    m = "".join(b)
    return code[m][CODE_DEFAULT]

def get_strip_color(img, pos, h):
    p1 = img.getpixel((pos, h // 2))
    p2 = img.getpixel((pos, h // 4))
    p3 = img.getpixel((pos, 3 * h // 4))
    avg = (((p1[0] + p2[0] + p3[0]) // 3) + ((p1[1] + p2[1] + p3[1]) // 3) + ((p1[2] + p2[2] + p3[2]) // 3)) // 3 # overkill as fuck
    if avg > 127:
        return "0" # white
    return "1" # black

def analyse_image(d, code):
    data = b64decode(d)
    img = Image.open(BytesIO(data))
    charlen = img.width // 11
    bits = [[] for _ in range(charlen)]
    for i in range(img.width):
        bits[i // 11].append(get_strip_color(img, i, img.height))
    r = ""
    if CRC_PRESENT:
        del bits[-1] # if there's a control sum, the last byte is not part of the code 
    for b in bits:
        r += get_char(b, code)
    return r

def main():
    code = create_mapping()
    nc = remote("challenge.404ctf.fr", 30566)
    for _ in range(128):
        print(nc.readlineS())
        sb64 = nc.readlineS().strip()
        print(sb64)
        r = analyse_image(sb64, code)
        print(r)
        nc.sendline(r.encode())
        print(nc.readlineS())
    nc.stream()

main()
