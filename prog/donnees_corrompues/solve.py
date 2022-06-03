#!/usr/bin/env python3

from pwn import *

dico = {
    "A": "000000",
    "B": "000001",
    "C": "000010",
    "D": "000011",
    "E": "000100",
    "F": "000101",
    "G": "000110",
    "H": "000111",
    "I": "001000",
    "J": "001001",
    "K": "001010",
    "L": "001011",
    "M": "001100",
    "N": "001101",
    "O": "001110",
    "P": "001111",
    "Q": "010000",
    "R": "010001",
    "S": "010010",
    "T": "010011",
    "U": "010100",
    "V": "010101",
    "W": "010110",
    "X": "010111",
    "Y": "011000",
    "Z": "011001",
    "a": "011010",
    "b": "011011",
    "c": "011100",
    "d": "011101",
    "e": "011110",
    "f": "011111",
    "g": "100000",
    "h": "100001",
    "i": "100010",
    "j": "100011",
    "k": "100100",
    "l": "100101",
    "m": "100110",
    "n": "100111",
    "o": "101000",
    "p": "101001",
    "q": "101010",
    "r": "101011",
    "s": "101100",
    "t": "101101",
    "u": "101110",
    "v": "101111",
    "w": "110000",
    "x": "110001",
    "y": "110010",
    "z": "110011",
    "0": "110100",
    "1": "110101",
    "2": "110110",
    "3": "110111",
    "4": "111000",
    "5": "111001",
    "6": "111010",
    "7": "111011",
    "8": "111100",
    "9": "111101",
    "+": "111110",
    "/": "111111",
}

transcode = {
    "А": "A",
    "Т": "T",
    "х": "x",
    "о": "o",
    "у": "y",
    "Н": "H",
    "е": "e",
    "В": "B",
    "а": "a",
    "К": "K",
    "р": "p",
    "с": "c",
    "à": "a",
    "é": "e",
}


def get_b64(c, spaces=False):
    c = transcode.get(c, c)
    if not c.isascii():
        print(f"Not ascii : {c}")
    if spaces and c == "=":
        return "000000"
    return dico.get(c, "")


def pad(s):
    l = len(s)
    if l % 8 == 0:
        return s
    p = "0" * (l % 8)
    return s.removesuffix(p)


def get_full_b64(d):
    r = ""
    for c in d:
        r += get_b64(c)
    return pad(r)


def get_bytes(s):
    return int(s, 2).to_bytes(len(s) // 8, byteorder="big")


def main():
    nc = remote("challenge.404ctf.fr", 30117)
    with open("result", "wb") as f:
        while True:
            try:
                x = nc.recvuntil(b"es : ")
            except EOFError:
                break
            data = nc.readline().decode("utf8").strip()
            res = get_full_b64(data)
            nc.sendline(res.encode("utf8"))
            f.write(get_bytes(res))
            nc.readlineS()


main()
