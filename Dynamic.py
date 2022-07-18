import Kaji


class LIFO:
    def __init__(self):
        self.stk = Kaji.LList()

    def pop(self):
        x = self.stk.tail.data
        self.stk.deletes(self.stk.size)
        return x

    def push(self, data):
        self.stk.inserts(data, self.stk.size + 1)

    def top(self):
        return self.stk.tail.data


class FIFO:
    def __init__(self):
        self.que = Kaji.LList()

    def enqueue(self, data):
        self.que.inserts(data, self.que.size + 1)

    def dequeue(self):
        x = self.que.head.data
        self.que.deletes(1)
        return x

    def front(self):
        return self.que.head.data
