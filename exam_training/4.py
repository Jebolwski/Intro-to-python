
class Car:
    def __init__(self, speed, name, price):
        self.speed = speed
        self.name = name
        self.price = price

    def __add__(self, right):
        return Car(right.speed+self.speed, self.name+" | "+right.name, self.price+right.price)

    def __mul__(self, right):
        return Car(right.speed*self.speed, self.name+" | "+right.name, self.price*right.price)

    def __iadd__(self, right):
        self.speed += right.speed
        self.price += right.price
        return self

    def __str__(self):
        return self.name + " ---- " + str(self.speed)+"km/s" + " ---- " + str(self.price) + "tl"


bugatti = Car(240, "bugatti", 12)
porche = Car(280, "porche", 10)

print(bugatti)

print(bugatti*porche)

bugatti += porche

print(bugatti)
