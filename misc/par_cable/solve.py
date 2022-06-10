#!/usr/bin/env python3

# we assume we already transformed the cable file with
# cat Cable.txt | sed -e "s/-1/0/g" | tr -d ' ' > stripped.txt

def main():
    with open("stripped.txt", "r") as f:
        s = f.read().strip()
    r = ""
    for i in range(len(s) - 1):
        x = str(int(s[i]) ^ int(s[i + 1]))
        s = s[:i] + x + s[i+1:]
        r += x
        if len(r) == 8:
            print(chr(int(r, 2)), end="")
            r = ""

main()

