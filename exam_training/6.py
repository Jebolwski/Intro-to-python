from dataclasses import dataclass, field


class Klass1:
    a = 1

    def __init__(self, b):
        self.b = b


print(Klass1.a)
klass = Klass1("23")
print(klass.a, klass.b)


@dataclass(order=True)
class Klass:
    ad: str
    soyad: str
    no: int
    _nicknames: list[str] = field(default_factory=list)


k = Klass("mert", "gogo", 4)
k1 = Klass("aert", "gogo", 4)
k2 = Klass("aert", "gogo", 4, ["crazboy", "xx_BeLaLi_xx"])


print(k2)
