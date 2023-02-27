

def func():
    num1 = int(input("Sayı 1 :"))
    num2 = int(input("Sayı 2 :"))
    num3 = int(input("Sayı 3 :"))

    if num1 >= num2 >= num3:
        print(num1, num2, num3)
        return

    if num1 >= num3 >= num2:
        print(num1, num3, num2)
        return

    if num2 >= num1 >= num3:
        print(num2, num1, num3)
        return

    if num2 >= num3 >= num1:
        print(num2, num3, num1)
        return

    if num3 >= num1 >= num2:
        print(num3, num1, num2)
        return

    if num3 >= num2 >= num1:
        print(num3, num2, num1)
        return

func()