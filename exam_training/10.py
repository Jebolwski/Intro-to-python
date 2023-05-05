def soru1():
    import math
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 1 : "))
    for i in range(math.ceil(math.sqrt(num1)), int(math.sqrt(num2))):
        print(i**2)


def soru2():
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 1 : "))
    x = max(num1, num2)
    while True:
        x += 1
        if x % num1 == 0 and x % num2 == 0:
            print(x)
            return


def soru3():
    class Dikdortgen:
        def __init__(self, yukseklik, genislik):
            self.yukseklik = yukseklik
            self.genislik = genislik

        def fitsInside(self, other):
            if (other.yukseklik > self.yukseklik and other.genislik > self.genislik) or (other.yukseklik > self.genislik and other.genislik > self.yukseklik):
                return True
            return False

    dik1 = Dikdortgen(10, 20)
    dik2 = Dikdortgen(15, 25)
    dik3 = Dikdortgen(25, 15)
    print(dik1.fitsInside(dik3))


def soru4():
    class Times:

        def __init__(self, hour, minute):
            self.hour = hour
            self.minute = minute

        def __add__(self, other):
            if other.minute+self.minute > 60:
                x = (other.minute+self.minute) % 60
                return Times(self.hour+other.hour+1, x)
            else:
                return Times(self.hour+other.hour, other.minute+self.minute)

        def __str__(self) -> str:
            return (str(self.hour)+":"+str(self.minute))

    time1 = Times(19, 40)
    time2 = Times(13, 40)
    print(time1+time2)


soru4()
