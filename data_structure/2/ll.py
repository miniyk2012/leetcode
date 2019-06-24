class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, v):
        if self.head is None:
            self.head = Node(v)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(v)

    def print(self):
        cur = self.head
        while cur:
            print(cur.v)
            cur = cur.next
    
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


def run():
    print('run!!!')


if __name__ == "__main__":
    n = Node(10)
    # a.py
    print(n.v, n.next)
    ll = LinkedList()   # []
    ll.add(10)          # [10]
    ll.add(2)           # [10, 2]
    ll.add(-3)          # [10, 2, -3]
    ll.print()          # 10, 2 , -3
    x = ll.pophead()        # [2, -3]
    print(f'x={x.v},next={x.next}')
    ll.print()

    # b.py
    ll = LinkedList()
    ll.add(run)
    ll.add(run)
    node = ll.pophead() # run
    node.v()