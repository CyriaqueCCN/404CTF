def tour1(password):
    string = str("".join("".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]


def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(
            password[password.index(password[i])]
            + password[password.index(password[i + 1 % len(password)])]
        )
        password.pop(password.index(password[i]))
        i += int("qkdj", base=27) - int("QKDJ", base=31) + 267500
    return new


def t2(pwd):
    # returns [0, 0+1, 1, 1+2, 2, 2+2]
    # simplification of tour2
    n = []
    while pwd != []:
        n.append(pwd[0])
        n.append(pwd[0] + pwd[1])  # if len > 1, else 2*pwd[0]
        pwd.pop(0)
    return n


def tour3(password):
    mdp = [
        "l",
        "x",
        "i",
        "b",
        "i",
        "i",
        "q",
        "u",
        "d",
        "v",
        "a",
        "v",
        "b",
        "n",
        "l",
        "v",
        "v",
        "l",
        "g",
        "z",
        "q",
        "g",
        "i",
        "u",
        "d",
        "u",
        "d",
        "j",
        "o",
        "r",
        "y",
        "r",
        "u",
        "a",
    ]
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i - 1] = chr(
            password[len(password) - i - 1] + i % 4
        ), chr(password[i] + i % 4)
    return "".join(mdp)


def rev3(pwd):
    # in  : str[34]
    # out : list[34]
    p = list(pwd)
    new = [0] * 34
    lp = len(p)
    for i in range(lp):
        new[i] = ord(p[lp - 1 - i]) - i % 4
        new[lp - 1 - i] = ord(p[i]) - i % 4
    return new


def rev2(pwd):
    r = [pwd[i] for i in range(len(pwd)) if i % 2 == 0]
    return r


def rev1(pwd):
    # takes [] of ord(c), returns str
    return "".join([chr(x) for x in pwd])[::-1]


def solve():
    password = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"
    print("404CTF{" + rev1(rev2(rev3(password))) + "}")


solve()
