class Stack():

    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        self.arr = self.arr[:len(self.arr) - 1]

    def peek(self):
        return self.arr[len(self.arr) - 1]

    def clear(self):
        self.arr = []

    def printstack(self):
        for i in range(len(self.arr) - 1, -1, -1):
            print('|', self.arr[i], '|')
        print()

print("STACK")
stack = Stack()

stack.push(1)
stack.push(2)

stack.printstack()

stack.push(3)
stack.push(4)


stack.printstack()

class Queue():

    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.insert(0, value)

    def pop(self):
        self.arr = self.arr[:len(self.arr) - 1]

    def clear(self):
        self.arr = []

    def printqueue(self):
        for i in self.arr[:len(self.arr) - 1]:
            print(str(i) + ", ", end="")
        print(self.arr[len(self.arr) - 1])

print("QUEUE")
queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

queue.printqueue()

queue.pop()

queue.printqueue()

def Oyun():
    import random

    def generaterand():
        string = ""
        for i in range(4):
            string += str(random.randint(0, 9))
        return int(string)

    num = generaterand()

    count = 1

    while True:
        inp = input("4 haneli rakamı tahmin edin : ")
        strnum = str(num)
        if inp == "q":
            print("Çıkış Yaptınız! Sayı", strnum, "idi.")
            break
        if strnum == inp:
            print("Doğru!", count, " denemede buldunuz.")
            break

        plus = 0
        star = 0

        for i in range(len(inp)):
            if inp[i] == strnum[i]:
                star += 1
            elif inp[i] in strnum and inp[i] != strnum[i] and inp.count(inp[i]) == 1:
                plus += 1
        tmp = star * "*" + plus * "+"
        print(tmp)
        count += 1


Oyun()
