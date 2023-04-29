import sys
arr = [i*2 for i in range(5)]

print("arr", arr)


def f():
    yield(10)
    yield(11)
    yield(12)


a = f()

print(next(a))
print(next(a))


a1 = (i*2 for i in range(100))
a2 = [i*5-1 for i in range(100)]

print(sys.getsizeof(a1))
print(sys.getsizeof(a2))


print("a2 filter", list(filter(lambda x: x % 2 != 0, a2)))

dp = {"mesi": 10, "ronaldo": 7}

print(dp)
# print(dp.keys())
# print(dp.values())


dp.update({"mesi": 11})
dp.update({"gattuso": 12})
dp.update(maldini=12)

print(dp)

s = {1, 2, 3, 4, "mesi", (1, 2)}

s1 = {1, 4, "mesi", (1, 2)}

print(s, type(s))

print(s1.issubset(s))

print(s.difference(s1))
