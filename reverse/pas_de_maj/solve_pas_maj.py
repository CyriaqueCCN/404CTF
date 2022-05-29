def inp():
    p = input("Pass ? : ")
    return [ord(e) for e in p]


KEY = "d1j#H(&Ja1_2 61fG&"


def op(e, l):
    # from bytecode
    x = (5 * e) ^ ord(KEY[l % len(KEY)])
    return [x]


def code(l):
    # Names : ord, key, len, code
    # Vars : l, el, rest
    # Constants : None, 1, 5, 0
    match l:
        case []:
            return []
        case [el, *rest]:
            return op(el, len(rest)) + code(rest)


def evaluate(s):
    return code([ord(e) for e in s])


def test():
    x = inp()
    print(x)
    print(code(x))


RES = [
    292,
    194,
    347,
    382,
    453,
    276,
    577,
    434,
    183,
    295,
    318,
    196,
    482,
    325,
    412,
    502,
    396,
    402,
    328,
    194,
    473,
    490,
    299,
    503,
    386,
    215,
    263,
    211,
    318,
    206,
    533,
]

DICO = "_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def bruteforce_pass():
    # test string : 404CTF{00000000000000000000000} because we need to test with fixed length (31)
    res_str = "404CTF{00000000000000000000000}"
    for i in range(len(res_str) - 1):
        j = 0
        while j < len(DICO):
            n_str = res_str[:i] + DICO[j] + res_str[i + 1 :]
            r = evaluate(n_str)
            if r[i] == RES[i]:
                res_str = n_str
                break
            else:
                j += 1
    print(res_str)


bruteforce_pass()
