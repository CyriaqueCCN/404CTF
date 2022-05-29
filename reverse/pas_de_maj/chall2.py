# Source Generated with Decompyle++
# File: chall.pyc (Python 3.10)

def inp():
    p = input("Pass ? : ")
    return [ ord(e) for e in p ])

KEY = 'd1j#H(&Ja1_2 61fG&'

def op(e, l):
    x = 5*e+ord(KEY[l % len(KEY)])
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

def o_code(l):
    # MATCH_SEQ
    pass
# WARNING: Decompyle incomplete

def test():
    x = inp()
    print(x)
    print(code(x))

def run():
    if code(inp()) == [
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
    533]:
        print('Bravo!')
    else:
        print('Dommage...')
