import numpy as np

array = np.array([1, 2, 3, 4, 5])

array.resize((2,3))

arr1=np.array([[1,2],[3,4]])

arr2 = np.random.randint(5,15,(2,4))

arr3 = np.random.randint(0,10,(2,4))

print(arr2.transpose())
print("==========")
print(arr2.transpose())
print("==========")
print(arr3)
arr3=np.multiply(arr3,arr2)
print(arr3)



print(arr2)
print("==========")
print(arr2>10)
print("==========")
print(arr2.mean()==(arr2.sum()/arr2.size))
