import random


for i in range(5):
    print(random.randrange(1,20))
for i in range(10):
    print("T" if random.randrange(2) == 0 else "F")


zar1 = random.randrange(1,7)
zar2 = random.randrange(1,7)

total=zar1+zar2
print(zar1,"+",zar2,"=",total)
if total == 7 or total == 11:
    print("Kazandınız")
elif total == 2 or total == 3 or total == 12:
    print("Kaybettiniz")
else:
    puan = total
    print("Puanınız =",puan)
    while True:
        zar1 = random.randrange(1, 7)
        zar2 = random.randrange(1, 7)
        total = zar1 + zar2
        print(zar1, "+", zar2, "=", total)
        if total == 7:
            print("Kaybettiniz")
            break
        elif puan == total:
            print("Kazandınız")
            break

t=(1,5)
# HATA
# for i in range(len(t)):
#     t[i]=4
print(type(t))
