from dataclasses import dataclass, field


@dataclass(eq=True, order=True)
class PriorityQueue:
    _arr: list = field(default_factory=list)

    # def __post_init__(self):
    #     print("ANK MAESİ")

    def insert(self, x):
        self._arr.insert(0, x)

    def pop(self):
        index = self._arr.index(max(self._arr))
        return self._arr.pop(index)

    def isEmpty(self):
        return len(self._arr) == 0

    def peek(self):
        return self._arr[-1]

    def __str__(self):
        string = ""
        for i in self._arr:
            string += "| "+str(i)+" |\n"
        string = string[:len(string)-1]
        return string

    def __repr__(self):
        string = ""
        for i in self._arr:
            string += "| "+str(i)+" |\n"
        string = string[:len(string)-1]
        return string


queue = PriorityQueue()
queue.insert(10)
queue.insert(15)
queue.insert(20)

queue1 = PriorityQueue()
queue1.insert(10)
queue1.insert(15)


print(queue)

print()

print(queue1)

print(queue > queue1)
print(queue < queue1)
