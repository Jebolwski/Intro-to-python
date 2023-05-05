from dataclasses import dataclass, field


@dataclass
class item:
    value: int
    priority: int

    def __str__(self):
        return "(" + str(self.value) + "|" + str(self.priority) + ")"


@dataclass
class pq:
    pr: list[item] = field(default_factory=list)

    def enqueue(self, value: int, priority: int):
        self.pr.append(item(value, priority))

    def peek(self):
        return self.pr[self.get_highest_priority_index()]

    def dequeue(self):
        ind = self.get_highest_priority_index()
        self.pr.pop(ind)

    def get_highest_priority_index(self):
        maksi, index = 0, 0
        for i in range(len(self.pr)):
            if self.pr[i].priority > maksi:
                index = i
                maksi = self.pr[i].priority

        return index

    def printQueue(self):
        for i in self.pr:
            print(i, end=" ")
        print()


queue = pq()
queue.enqueue(10, 1)
queue.printQueue()
queue.enqueue(4, 3)
queue.printQueue()
queue.enqueue(4, 34)
queue.printQueue()
queue.enqueue(4, 1)
queue.printQueue()
queue.dequeue()
queue.printQueue()
queue.dequeue()
queue.printQueue()
queue.dequeue()
queue.printQueue()
