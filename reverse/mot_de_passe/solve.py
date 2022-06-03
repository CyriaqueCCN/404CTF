PASSW = "4/2@PAu<+ViNgg%^5NS`#J\x1fNK<XNW(_"
# care about format of special chars : Java print \ux001f when python uses \x1f


def hide(s):
    i = 0
    res = ""
    while i < len(s):
        c = s[i]
        res += chr((ord(c) - i & 65535) % 128)
        i += 1
    return res


def rev_hide(c, i):
    x = ord(c) + i % 128
    return chr(x)


def rev():
    s = PASSW
    r = ""
    for i in range(len(s)):
        r += rev_hide(s[i], i)
    return r


def test_hide():
    p = hide(input("Pass ? "))
    print(p)
    print(p == PASSW)


# test_hide()
print(rev())
