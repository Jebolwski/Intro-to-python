import os
os.rename("2.txt", "1.txt")
print("messi")
a = 2

f = open("1.txt", "r")

for i in f:
    print(i)
    print("=============")

f.close()

f = open("1.txt", "w")

f.write("yapma")
f.close()

f = open("1.txt", "r")
for i in f:
    print(i)
    print("=============")

f.close()

with open("1.txt", "w") as f:
    f.write("husayin")
    print(" ben yoruldum", file=f)
