
    







def positivity(i,pos,neg,zero):
    if i > 0:
        return pos
    elif i < 0:
        return neg
    else:
        return zero

def loopsubp(i):
    while i > 0:
        print(i)
        i -= 1

def loopaddp(i,end):
    while i < end:
        i += 1
        print(i)

def looptimep(b,s,tb):
    while s < b:
        print(s)
        s *= tb

def loopdivp(b,s,db):
    while b > s:
        b /= db
        print(b)

def loopdivnrp(b,s,db):
    while b > s:
        b //= db
        print(b)

def loopexpp(b,s,eb):
    while s < b:
        print(s)
        s **= eb

def loopsqurp(b,s,sb):
    ssb = 1/sb
    while b > s:
        print(b)
        b **= ssb










def atbash_uno(text):
    
    atb_keydict = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
        "e": "v",
        "f": "u",
        "g": "t",
        "h": "s",
        "i": "r",
        "j": "q",
        "k": "p",
        "l": "o",
        "m": "n",
        "n": "m",
        "o": "l",
        "p": "k",
        "q": "j",
        "r": "i",
        "s": "h",
        "t": "g",
        "u": "f",
        "v": "e",
        "w": "d",
        "x": "c",
        "y": "b",
        "z": "a",
        "A": "Z",
        "B": "Y",
        "C": "X",
        "D": "W",
        "E": "V",
        "F": "U",
        "G": "T",
        "H": "S",
        "I": "R",
        "J": "Q",
        "K": "P",
        "L": "O",
        "M": "N",
        "N": "M",
        "O": "L",
        "P": "K",
        "Q": "J",
        "R": "I",
        "S": "H",
        "T": "G",
        "U": "F",
        "V": "E",
        "W": "D",
        "X": "C",
        "Y": "B",
        "Z": "A"
    }
    s = ""
    for i in text:
        if i in atb_keydict:
            s += atb_keydict[i]
        else:
            s += i
    return s

def CONST_GROUP(type):

    CONST_HELLO = "Hello, World!"
    CONST_GOODBYE = "Goodbye, World!"
    CONST_FAREWELL = "Farewell, World!"
    CONST_END = "The End."

    if type == "greeting":
        return CONST_HELLO
    elif type == "farewell":
        return CONST_GOODBYE
    elif type == "parting":
        return CONST_FAREWELL
    elif type == "end":
        return CONST_END
    else:
        return 0




def end():
    while True:
        print("end")
