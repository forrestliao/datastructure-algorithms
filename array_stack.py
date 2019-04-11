class ArrayStack:
    def __init__(self):
        self.top = 0
        self.stack = list()
    def print_stack(self):
        if not self.is_empty():
            print(self.stack[:self.top])
        else:
            print("it's empty")
    def is_empty(self):
        return self.top == 0
    def push(self, num):
        if len(self.stack)>self.top:
            self.stack[self.top] = num
        else:
            self.stack+= [num]
        self.top+=1
    def pop(self):
        if not self.is_empty():
            self.top-=1
        else:
            print("it's empty.")


if __name__=="__main__":
    stack1 = ArrayStack()
    stack1.push(14)
    stack1.push(9)
    stack1.pop()
    stack1.push(7)
    stack1.push(9)
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.print_stack()