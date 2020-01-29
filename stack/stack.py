class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()
    def dis(self):
        return "stack:" + str(self.stack)


s = Stack()
s.push(20)
s.push(30)
s.push(40)
s.pop()
print(s.dis())
