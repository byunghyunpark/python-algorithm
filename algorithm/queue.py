class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next_node = newNode
            self.tail = newNode

    def dequeue(self):
        if self.is_empty():
            raise StopIteration

        retData = self.head.data

        self.head = self.head.next_node
        return retData

    def peek(self):
        if self.is_empty():
            raise StopIteration

        return self.head.data

    def __iter__(self):
        return self

    def __next__(self):
        return self.dequeue()


def play_queue():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    for data in queue:
        print(data)