def deneme():
    print("deneme")


def fakt(x):
    """"DOCSTRING ACIKLAMA"""
    out = 1
    for i in range(1, x + 1):
        out *= i
    print(out)
    return out


def topla(x, y):
    return x + y


def ustalma(x, y):
    return x ** y




def goal(assist, minute, scorer="messi", ):
    print("GOLAZO", scorer, assist, minute)


def add(*x):
    out = 0
    print(type(x))
    for i in x:
        out += i
    print(out)


def addwithoperator(operator,mesi,*nums):
    print(nums)
    if operator=="+":
        out=0
        for i in nums:
            out+=i
        return out
    if operator=="*":
        out = 1
        for i in nums:
            out *= i
        return out

print(addwithoperator("*",3, 5, 7, 3))


def faktor(x):
    pass

print(faktor(5))