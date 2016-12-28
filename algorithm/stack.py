class Node:
    """
    노드를 초기화합니다.
    """
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class Stack:
    """
    stack을 구현합니다.
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """head node 존재 확인"""
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        """
        기존 head를 next node로 넘기고,
        head에 new node를 삽입
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def pop(self):
        """
        현재 head를 출력하고,
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
        return self.pop()


def play_stack():
    """stack 실행"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    for data in stack:
        print(data)
