import numpy as np

a=np.array([1,2,3])

# print(a,type(a))

b=np.array([[1,2,3],[4,5,6]])

print(b,b.shape,b.ndim)

c=np.array([i*3.1 for i in range(10)])

print(c.dtype)


for i in b:
    for j in i:
        print(j,end=" ")
    print()

print(np.zeros(10))
print(np.ones(10))

print(np.ones((2,5),dtype=int))

print(np.arange(40))

print(np.linspace(0.0,2.0,num=10))
print(np.linspace(0.0,2.0,num=10,dtype=int))

print("ÖNCE")
print(b)

b.resize(3,2)

print("SONRA")
print(b)

print("ÖNCE")
print(a)

a=a**3

print("SONRA")
print(a)


print(np.full(10,3))

print(np.eye(2,2))

print(np.random.random(size=(3,4)))

x = np.random.randint(10,size=(3,4))

z = np.array([3,2,5,5])

print("x",x)
print("z",z)

print(np.multiply(x,z))

u=x.transpose()

print(np.dot(x,u))


fonk=np.vectorize(lambda x: len(x)>3)

den = np.array(["mesi","ronaldo","ankra"])

print(fonk(den))


x=np.random.randint(5,20,size=(4,6))

y=x>10

print(x)

print(y)

print(x[y])

ar=np.random.randint(0,10,size=(4,))

print(ar,ar.max(),ar.mean(),ar.sum())




