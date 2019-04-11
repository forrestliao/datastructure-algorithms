class ArrayQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.queue = list()
    def is_empty(self):
        if self.queue:
            return False
        else:
            return True

    def is_full(self):
        if not self.is_empty():
           if self.front == self.rear:
               return True
        else:
            return False
        
    def double_capacity(self):
        self.queue = self.queue[self.front:] + self.queue[:self.rear]
        self.rear = self.capacity
        self.capacity*= 2
        self.front = 0

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
            self.front= (self.front+1)%self.capacity

    def push(self, num):
        if self.is_full():
            self.double_capacity()
        if self.rear < self.front:
            self.queue[self.rear] = num
        else:
            self.queue+= [num]
        self.rear = (self.rear+1)%self.capacity

if __name__ == "__main__":
    queue1 = ArrayQueue(5)
    queue1.push("A")
    queue1.push("B")
    queue1.push("C")
    queue1.push("D")
    queue1.push("E")
    queue1.pop()
    queue1.push("F")
    queue1.pop()
    queue1.push("G")
    queue1.push("H")
    queue1.push("I")
    queue1.pop()
    queue1.pop()
    queue1.pop()
    queue1.push("J")
    queue1.push("K")
    queue1.push("L")
    queue1.push("M")
    queue1.push("N")
    queue1.push("O")
    queue1.push("P")
    print("c:{},f:{},r:{},q:{}".format(queue1.capacity, queue1.front, queue1.rear, queue1.queue))
    queue1.print_queue()









