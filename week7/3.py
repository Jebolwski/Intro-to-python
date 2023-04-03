# Ödev 1
str1 = input("String 1 : ")
str2 = input("String 2 : ")

ch = input("Karşılaştırma ASCII ye mi Uzunluğuna göre mi karşılaştırılsın (a,u) : ")

if ch == 'a':
    if str1 > str2:
        print(str1, ">", str2)
    elif str1 < str2:
        print(str2, ">", str1)
    else:
        print(str1, "==", str2)

elif ch == 'u':
    if len(str1) > len(str2):
        print(str1, ">", str2)
    elif len(str1) < len(str2):
        print(str2, ">", str1)
    else:
        print(str1, "==", str2)

# Ödev 2


def compress(s):
    res = ""
    c = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            c += 1
        else:
            res = res + s[i - 1]
            if c > 1:
                res += str(c)
            c = 1
    res = res + s[-1]
    if c > 1:
        res += str(c)
    return res


print(compress("AAAAAAABCBCBCDRSADAX"))
