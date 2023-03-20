l = []

for i in range(6):
    l.append("messi")

print(l)

l2 = [i ** 2 for i in range(4)]

l3 = ["ankara", "messi", "ronaldo"]

l4 = [i * 2 for i in l3]

l5 = [i.upper() for i in l3]

print(l5, l4)

# generator object

l5 = (i for i in l3)

print(type(l5))


def mesi(i):
    print("aaaaa", end=" ")
    return i * 3


print(l5)

g = (mesi(i) for i in l2)
l = [mesi(i) for i in l2]

import sys

for i in g:
    print(i)

print(sys.getsizeof(g))
print(sys.getsizeof(l))

# lambda notation

print(list(filter(lambda x: x % 2 != 0, l2)))

print(tuple(map(lambda x: x ** 3, l2)))

l2 = list(range(5))

mesii = [i ** 2 if i % 2 != 0 else i for i in l2]

print(mesii)

# hata
# for i,j in l2,l3:
#     print(i,j)

print([i + j for i, j in zip(l2, l2)])

for i, j in zip(l2, l3):
    print(i, j)

dp = {2: 4, 1: 2, "a": "messi"}
dp1 = {2: 4, 1: 2, "a": "messi1"}

print(dp == dp1)

for i in dp.items():
    print(i)

b = dp.keys()  # shallow copy

b = dp.copy().keys()  # deep copy

print(b)

dp["ronaldo"] = "goat"

print(b)

for i in b:
    print(i)


d={}

text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's " \
     "standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to " \
     "make a type specimen book. It has survived not only five centuries, but also the leap into electronic " \
     "typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset " \
     "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker " \
     "including versions of Lorem Ipsum."


for i in text.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)

x={"a":[1,2,34,5,6],"b":[53,2,7,2,1,6]}
lst={i:j**2 for i,j in x}

print(lst)

sett= {2,5,"sad",(3,2)}

print(type(sett))