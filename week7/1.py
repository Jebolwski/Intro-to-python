# string işlemleri

from decimal import Decimal
print(f'{13232.34343:.2f}')

print(f'{1:.2f}')

print(f'{97:c}')


print(f'{Decimal("162.231"):.2f}')

print(f'{25:6d}')

s1 = "mesi"

# string karşılaştırma sorar

stri = "immens messi ank messi ank messi"

print(stri.count("messi", 14))

print(stri.count("messi"))

print(stri.index("messi"))

print(stri.rindex("messi"))

print("imemens" in stri)

print("immens" in stri)


print(stri)

print(stri.replace("messi", "ronaldo"))

arr = ["mes", "imes", "ime", "ims"]

wot = "**".join(arr)

print(wot)

s2 = "ank"

s1 += "  "+s2

print("*"*10)

print(s1)

print("aaa : asdad : bbb".partition(":"))

lor = """Lorem ipsum dolor sit amet, consectetur adipis
Lorem ips
+ veri
"""

print(lor.splitlines(keepends=False))

print(lor.splitlines(keepends=True))
