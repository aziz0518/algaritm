# Stack => LIFO => Last In First Out
# Queue => FIFI => First In First Out
arr = [10, 20, 30]
arr.append()
arr.pop
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            print(f'Popped {item}')
        return 'Stack is empty!'

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Stack is empty!'

    def size(self) -> int:
        return len(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push('apple')
stack.push('banana')
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.is_empty())

# Deque
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.popleft()
            return
        return 'Queue is empty ! '

    def peek(self):
        if not self.is_empty():
            return self.queue[-1]
        return 'Queue is empty ! '

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.dequeue()
queue.dequeue()
print(queue.queue)
