class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def setNext(self, node):
        self.next = node

    def getNext(self):
        return self.next

    def getData(self):
        return self.data


class LList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.size = 0

    def inserts(self, data, pos):
        previous = self.head
        current = self.head.getNext()
        newnode = Node()
        newnode.setData(data)
        if pos < 1 or pos > self.size + 1:
            print("Error: please enter a valid position.")
        elif pos == 1:
            if self.size == 0:
                self.head = newnode
            else:
                newnode.setNext(self.head)
                self.head = newnode
            self.size += 1
        else:
            for i in range(pos-2):
                previous = previous.getNext()
                current = current.getNext()
            if current is None:
                self.tail = newnode
            previous.setNext(newnode)
            newnode.setNext(current)
            self.size += 1

    def deletes(self, pos):
        previous = self.head
        current = self.head.getNext()
        if self.size == 0:
            print("The list is empty.")
        elif pos < 1 or pos > self.size:
            print("Error: please enter a valid position.")
        elif pos == 1:
            previous.setNext(None)
            self.head = current
            self.size -= 1
        else:
            for i in range(pos-2):
                previous = previous.getNext()
                current = current.getNext()
            if current.getNext:
                self.tail = previous
            previous.setNext(current.getNext())
            current.setNext(None)
            self.size -= 1

    def searches(self, data):
        previous = self.head
        for i in range(self.size):
            if previous.data == data:
                return i + 1
            previous = previous.getNext()
            if previous is None:
                print("Error: Data not found")

    # Optional method to display all nodes in the linked list.
    def display(self):
        A = self.head
        for i in range(self.size):
            if A.getNext() is None:
                print(f'{A.data}-> None')
            else:
                print(f'{A.data}-> ', end='')
            A = A.getNext()
