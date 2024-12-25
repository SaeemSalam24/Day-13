# Stack implementation using a list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty! Nothing to peek."
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

s = Stack()
s.push(5)
s.push(10)
s.push(15)

print("Stack:", s.display()) 
print("Top element:", s.peek())  
print("Popped element:", s.pop())  
print("Stack after pop:", s.display())  
print("Is stack empty?", s.is_empty())  
s.pop()
s.pop()
print("Stack after clearing:", s.display())  
