class Stack:
    def __init__(self):
        self.st = []
        self.counter = 0

    def push(self, val):
        self.st.append(val)

    def pop(self):
        val = self.st[-1]
        del self.st[-1]
        self.counter += 1
        return val

    def get_counter(self):
        return self.counter
    
stk = Stack()

for i in range(100):
    stk.push(i)

for i in range(100):
    print(stk.pop())

print(stk.get_counter())