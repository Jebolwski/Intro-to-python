def func1():
    a = 5
    b = 4.5
    c = "ankara messi"
    print(type(c))
    print(type(b))
    print(type(a))
    print(type(None))
    print(2 ** 3 ** 2)
    print(0.1 + 0.2)
    print(2 // 7)
    print(8 // 7)
    print(5 // 3)
    print(5 / 3)
    print("merhaba dünya")
    print("merb ben 'mahmud'")
    print("merb ben \"mahmud\"")
    print("lorem sip dum amet \
    ank messi")
    if False:
        num1 = input("bir sayı giriniz : ")
        if num1.isnumeric():
            num1 = int(num1)
        num2 = input("bir sayı giriniz : ")
        if num2.isnumeric():
            num2 = int(num2)
        if type(num1) == int and type(num2) == int:
            print(num1 + num2)
    print(10 < 11 < 13)
    if 0 < 10:
        print("ank")
        if 0 > 5:
            print("ronaldo")
        print("kamera")
    f = "messi" if 10 > 12 else "ronaldo"
    x = 10
    if x >= 100:
        print("ismail köybaşı")
    else:
        print("nigel benn")

    for i in range(5):
        print(i)

    print(1, 2, 3, 4, 5, 6, 7, sep="messi")

    for i in range(10):
        print(f"{i:>4}")

    for i in range(10):
        if i == 4:
            continue
        print(i)
    print("===========")
    for x in range(5):
        for i in range(10):
            if i == 5:
                break
            print(x, i)


func1()
# ! çıktı ne olur sorusu sorar

# ctrl + space
