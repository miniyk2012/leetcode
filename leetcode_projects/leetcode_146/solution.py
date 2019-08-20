from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Node:
    key: int
    val: int
    pre: "Node" = field(default=None, repr=False)
    nxt: "Node" = field(default=None, repr=False)


class LinkedList:
    def __init__(self):
        self._root = None
        self._tail = None

    def append(self, node: Node) -> None:
        if self._tail:
            self._tail.nxt, node._pre, self._tail = node, self._tail, node
        else:
            self._root = self._tail = node

    def appendHead(self, node: Node) -> None:
        if self._root:
            self._root.pre, node.nxt, self._root = node, self._root, node
        else:
            self._root = self._tail = node

    def pop(self) -> Node:
        if self._root is None:
            raise RuntimeError('LinkedList is empty, cant\'t pop')
        node, self._tail, node.pre = self._tail, self._tail.pre, None
        if self._tail is None:
            self._root = None
        else:
            self._tail.nxt = None
        return node

    def pick(self, node: Node) -> None:
        """将node排到第一位, 假设node一定在链表中"""
        if node.pre is None:
            return
        if node.nxt is None:
            self.pop()
        else:
            node.pre.nxt, node.nxt.pre = node.nxt, node.pre
        node.pre, node.nxt, self._root.pre, self._root = None, self._root, node, node

    def __str__(self):
        ret = ''
        current: Node = self._root
        while current:
            ret += str(current) + '->'
            current = current.nxt
        return ret


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self.nodes: Dict[int, Node] = {}
        self.linkedList: LinkedList = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.linkedList.pick(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self.linkedList.pick(node)
            return

        if len(self.nodes) == self._capacity:
            pop_node = self.linkedList.pop()
            self.nodes.pop(pop_node.key)

        node = Node(key, value)
        self.nodes[key] = node
        self.linkedList.appendHead(node)


def testLinkedList():
    node1: Node = Node(1, 1)
    node2: Node = Node(2, 2)
    node3: Node = Node(3, 3)
    node4: Node = Node(4, 4)
    linkList: LinkedList = LinkedList()
    linkList.appendHead(node1)
    linkList.appendHead(node2)
    linkList.pick(node1)
    linkList.pop()
    linkList.appendHead(node3)
    linkList.pop()
    linkList.appendHead(node4)
    linkList.pick(node3)
    linkList.pick(node4)
    print(linkList)


def test1():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # 该操作会使得key=2作废
    assert cache.get(2) == -1  # 返回 - 1(未找到)
    cache.put(4, 4)  # 该操作会使得key=1作废
    assert cache.get(1) == -1  # 返回 - 1(未找到)
    assert cache.get(3)  # 返回3
    assert cache.get(4) == 4  # 返回4


if __name__ == '__main__':
    # testLinkedList()
    test1()
