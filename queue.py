import numpy as np

class ArrayQueue:

    queue = []
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    def is_full(self):
        if (self.rear)%self.capacity==self.front:
            return True
        else:
            return False
    def double_capacity(self):
        new_queue = self.queue[self.front:]+self.queue[:self.rear]
        self.queue = new_queue
        del new_queue
        self.capacity *=2
    def print_queue(self):
        if self.is_empty():
            print("This queue is empty.")
        elif self.rear > self.front:
            print("The queue is {}.".format(self.queue[self.front:self.rear]))
        else:
            print("The queue is {}.".format(self.queue[self.front:]+self.queue[:self.rear]))
    def pop(self):
        if self.is_empty():
            print("This queue is empty,you can't dequeue")
        else:
            self.front=(self.front+1)%self.capacity
    def push(self, num):
        if self.is_full():
            self.double_capacity()
        self.queue+= [num]
        self.rear = (self.rear+1)%self.capacity
if __name__ == "__main__":
    queue1 = ArrayQueue(5)
    queue1.push("A")
    queue1.push("B")
    queue1.push("C")
    queue1.push("D")
    queue1.push("E")
    queue1.push("F")
    queue1.pop()
    queue1.pop()
    queue1.push("G")
    queue1.pop()

    queue1.print_queue()









