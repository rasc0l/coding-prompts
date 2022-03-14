import heapq

class Stack:
    def __init__(self):
        self.data = []
        self.max_stack = []
        
    def push(self, elem):
        if not self.max_stack:
            self.max_stack.append(elem)
        if elem >= self.get_max():
            self.max_stack.append(elem)
        self.data.append(elem)
        
    def pop(self):
        result = self.data.pop()
        if result == self.get_max():
            self.max_stack.pop()
        return result
        
    def get_max(self):
        return self.max_stack[-1]
    
my_stack = Stack()

my_stack.push(1)
my_stack.push(4)
print(my_stack.get_max())
my_stack.push(2)
print(my_stack.get_max())
my_stack.pop()
my_stack.pop()
print(my_stack.get_max())
        