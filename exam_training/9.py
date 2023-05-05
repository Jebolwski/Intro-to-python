import random


def func():
    zar1 = random.randint(1, 6)
    zar2 = random.randint(1, 6)
    total = zar1+zar2
    if total == 7 or total == 11:
        print("Kazandınız.")
        return
    elif total in [2, 3, 12]:
        print("Kazandınız.")
        return
    elif total in [2, 3, 12]:
        print("Kaybettiniz.")
        return
    else:
        while True:
            zar1 = random.randint(1, 6)
            zar2 = random.randint(1, 6)
            print("("+str(zar1)+","+str(zar2)+") :", zar1+zar2, "|", total)
            if zar1+zar2 == 7:
                print("Kaybettiniz.")
                return
            elif zar1+zar2 == total:
                print("Kazandınız.")
                return


func()

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = [i*2 if i % 2 == 0 else i/2 for i in l1]

l3 = [2, 5]

print(l2)

for i, j in zip(l1, l3):
    print(i, j)
