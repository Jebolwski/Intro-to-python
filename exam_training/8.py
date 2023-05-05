from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Node:
    val: int
    next: Node | None = None


@dataclass
class LinkedList:
    root: Node | None = None

    def addtoend(self, node):
        if self.root == None:
            root = node
        else:
            temp = self.root
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def addtohead(self, node):
        node.next = self.root
        self.root = node

    def removefromend(self):
        temp = self.root
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def removefromhead(self):
        if self.root != None:
            self.root = self.root.next
        else:
            print("Boş")

    def printlist(self):
        temp = self.root
        while temp != None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print()


list = LinkedList(Node(4))
list.addtoend(Node(6))
list.addtoend(Node(7))
list.addtoend(Node(9))
list.addtohead(Node(11))
list.printlist()
list.removefromend()
list.printlist()
list.removefromhead()
list.printlist()
