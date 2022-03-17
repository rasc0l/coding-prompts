class Stack:
    def __init__(self):
        self.data = []
        self.max_stack = []
        
    # Push onto  max _tack only if it's a new max or data is empty
    def push(self, elem):
        if not self.data or elem >= self.get_max():
            self.max_stack.append(elem)
        self.data.append(elem)
        
    # Pop max_stack only if the element being popped is equal to the top value in the max_stack
    def pop(self):
        if not self.data:
            raise Exception('Stack is empty')
        if self.data[-1] == self.get_max():
            self.max_stack.pop()
        return self.data.pop()
        
    # Check last element added to the max_stack
    def get_max(self):
        if not self.data:
            raise Exception('Stack is empty')
        return self.data[-1] if not self.max_stack else self.max_stack[-1]
    
my_stack = Stack()

my_stack.push(1)
my_stack.push(4)
print(my_stack.get_max())
my_stack.push(2)
print(my_stack.get_max())
my_stack.pop()
my_stack.pop()
print(my_stack.get_max())
my_stack.pop()
# my_stack.pop() -- raises exception
my_stack.get_max()