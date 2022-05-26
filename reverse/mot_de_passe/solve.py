passw = "4/2@PAu<+ViNgg%^5NS`#J\\AA001fNK<XNW(_" # AA = ux
       #"404CTF{C3_sYst3mE_es7_rki[xoyK"
       #"404CTF{C3_sYst3mE_es7_rtpIJL~ki[xoyK}"

def hide(s):
    i = 0
    res = ""
    while i < len(s):
        c = s[i]
        res += chr((ord(c) - i & 0xffff) % 0x80)
        i += 1
    return res

def rev_truc(c, i):
    # 75 au lieu de 125
    x = (ord(c) + i)# & 0xffff)
    if x > 127:
        x = 128 - (x % 128)
    return chr(x)# % 128)

def rev(s):
    r = ""
    for i in range(len(s)):
        r += rev_truc(s[i], i)
    return r


print(rev(passw))
