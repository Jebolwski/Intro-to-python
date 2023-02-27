count = int(input("Kaç kere dönsün : "))

total = 0
for i in range(count):
    total+=int(input("Numara: "))

print("Toplam sayı :",total)
print("Ortalama :",total/count)

i=0
total=0
while i<count:
    i+=1
    total+=int(input("Numara: "))

print("Toplam sayı :",total)
print("Ortalama :",total/count)