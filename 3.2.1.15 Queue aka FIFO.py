class QueueError(Exception):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.elements = []

    def put(self, elem):
        self.elements.insert(0, elem)

    def get(self):
        if len(self.elements) == 0:
            raise QueueError()
        else:
            return self.elements.pop()
                


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
