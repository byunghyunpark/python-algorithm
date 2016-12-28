class Node:
    """
    node를 초기화합니다.
    """
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Queue:
    """
    queue를 구현합니다.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """head node 존재 확인"""
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, data):
        """
        tail에 new node를 삽입
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """
        head를 출력하고,
        head의 next node를 head에 삽입
        """
        if self.is_empty():
            raise StopIteration

        ret_data = self.head.data

        self.head = self.head.next_node
        return ret_data

    def peek(self):
        """current 확인"""
        if self.is_empty():
            raise StopIteration

        return self.head.data

    def __iter__(self):
        return self

    def __next__(self):
        return self.dequeue()


def play_queue():
    """queue 실행"""
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    for data in queue:
        print(data)
