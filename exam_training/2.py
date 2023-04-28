import pandas as pd
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 67]])
b = np.array([1, 2, 3])


print(a)
print(a.shape)
print(b.shape)
print(b.ndim)
print("b.dtype :", b.dtype)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()


print("np.zeros(10) =", np.zeros((2, 4)))
print("np.ones(10) =", np.ones((2, 4)))

print("np.linspace(0, 10, 10) =", np.linspace(0, 10, num=10))

# shallow copy ikisinide etkiler
# deep copy yepyeni bir obje verir

a_reshaped = a.reshape(3, 2)
print(a_reshaped)
print(b*3)

new_arr1 = np.full((2, 4), 2)
new_arr2 = np.eye(4)

print("new_arr1 =", new_arr1)
print("new_arr2 =", new_arr2)


print(new_arr2 > 0)

print("new_arr2.transpoze()", new_arr2.transpose())

print(new_arr1.min())

print("=========PANDAS==========")


a = pd.Series([1, 323, 4])
b = pd.Series([10, range(5)])

print(a)

print(b)

print(a[1])

print(a.count())

df = pd.DataFrame({"A": [2, 3], "B": [3, 4], "C": ("asşdj", "ğdfks")})

df.index = ["I", "II"]

print(df)
