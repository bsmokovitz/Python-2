class Queue:
    def __init__(self):
        self.que = []

    def put(self, elem):
        self.que.insert(0, elem)

    def get(self):
        if len(self.que) == 0:
            return
        return self.que.pop()
    
    def is_empty(self):
        return len(self.que) == 0
    
que = Queue()

que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        if que.get() == None:
            pass
        else:
            print(que.get())
except IndexError:
    print("Queue empty")

print(que.is_empty())