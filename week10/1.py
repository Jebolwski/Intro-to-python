import random
from dataclasses import dataclass, field
from collections import namedtuple

Hoca = namedtuple('Hoca', ["Yaş", "Baş"], defaults=["yasso", "basso"])

hoca = Hoca(20, "baş")

arr = [121, "şaskda"]

hoca1 = Hoca._make(arr)

hoca2 = Hoca()

print(hoca.Baş)
print(hoca.Yaş)
print(hoca)
print(hoca1)
print(hoca2)


@dataclass(order=True)
class Pano:
    num: float = field(init=False, default_factory=random.random)
    num1: float = field(repr=False, init=False, default_factory=random.random)


pan = Pano()
print(pan.num)
print(pan)
