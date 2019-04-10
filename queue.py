import numpy as np

class array_queue:

    queue = []
    def __init__(self, capacity, front = 0, rear = 0):
        self.capacity = capacity
        self.front = front
        self.rear = rear
    def is_empty(self):
        if self.front == self.rear:
            return True
        else:
            return False
    def is_full(self):
        if (self.rear+1)%self.capacity==self.front:
            return True
        else:
            return False
    def double_capacity(self):
        new_queue = []
    def print_queue(self):
        if self.is_empty():
            print("This queue is empty.")
        else:
            print("The queue is {}.".format(self.queue[self.front:self.rear]))
    def pop(self):
        if self.is_empty():
            print("This queue is empty.")
        else:
            self.front=(self.front+1)%self.capacity
    def push(self):


