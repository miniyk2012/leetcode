class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, v):
        if self.head is not None:
            self.head.add(v)
            return
        self.head = Node(v)

    def print(self):
        if self.head:
            self.head.print()

    def pophead(self):
        if self.head is None:
            raise Exception('链表为空')

        head = self.head
        self.head = head.next
        head.next = None
        return head


class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

    def print(self):
        print(self.v)
        if self.next:
            self.next.print()

    def add(self, v):
        if self.next is not None:
            return self.next.add(v)
        self.next = Node(v)


def run():
    print('run!!!')


def count_recursion(n):
    if n > 1:
        count_recursion(n - 1)
    print(n - 1)


if __name__ == "__main__":
    n = Node(10)
    # a.py
    print(n.v, n.next)
    ll = LinkedList()  # []
    ll.add(10)  # [10]
    ll.add(2)  # [10, 2]
    ll.add(-3)  # [10, 2, -3]
    ll.print()  # 10, 2 , -3
    print()
    count_recursion(4)

"""
python 中 deque is a doubly linked list while List is just an array.
"""