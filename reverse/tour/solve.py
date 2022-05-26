def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]

def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    return new

def t2(pwd):
    # returns [0, 0+1, 1, 1+2, 2, 2+2]
    n = []
    while pwd != []:
        n.append(pwd[0])
        n.append(pwd[0] + pwd[1]) # if len > 1, else 2*pwd[0]
        pwd.pop(0)
    return n

def tour3(password):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i -1 ] + i % 4),  chr(password[i] + i % 4)
    return "".join(mdp)

def t3(pwd):
    r = []
    imax = len(pwd)
    for i in range(imax):
        r[i] = chr(pwd[imax - 1 - i] + i)
        r[imax - 1 - i] = chr(pwd[i] + i)
    return "".join(r)

def rev3(pwd):
    p = list(pwd)
    new = [0] * 34
    lp = len(p)
    print(lp)
    for i in range(lp):
        new[i] = ord(p[lp - 1 - i]) - i
        new[lp - 1 - i] = ord(p[i]) - i
    print(new)
    return new

mdp = "x"#input("Mot de passe : ")
password = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"

hexpass = "c2a150c28736c2a873c38955c28531c28654c28330c29564c2b856c38a76c3a775c2a936c28452c38878c2a83478467735"
np = bytes.fromhex(hexpass)#.decode('ascii')

password = np.decode()

#if tour3(tour2(tour1(mdp))) == password:
#    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
#else :
#    print("Désolé, le mot-de-passe n'est pas correct")

# reverse t3 with pass (takes str, returns [])
# reverse t2 with t3 result (takes [], returns [])
# reverse t1 with t2 result (takes [], returns str)
# got pass (str)

def r3(pwd):
    # takes str, returns [ord(x)]
    ...

def rev2(pwd):
    r = [pwd[i] for i in range(len(pwd)) if i % 2 == 0]
    print("Rev2 : ", r)
    return r

def rev1(pwd):
    # takes [] of ord(c), returns str
    r = [chr(x) for x in pwd]
    res = "".join(r)
    print(res)
    return res[::-1]#"".join([chr(x) for x in pwd])[::-1]

print("Le reverse du mdp est 404CTF{" + rev1(rev2(rev3(password))) + "}")
