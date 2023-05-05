def a():
    ad = input("Adı : ")
    soyad = input("Soyadı : ")
    okul_no = input("Okul No : ")

    sifre = ad[0]+ad[-1]+soyad[0]+soyad[-1]

    total = 0
    for i in okul_no[len(okul_no)-4:]:
        if int(i) % 2 == 1:
            total += int(i)

    sifre += str(total)

    print(sifre)


def b():
    arr = []
    a = input("sayı : ")
    if str.isnumeric(a):
        a = int(a)
        for i in range(1, a):
            if a % i == 0:
                arr.append(i)
        print(arr)
    else:
        print("sayı girmediniz.")


b()
