# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        relation_map = {}
        new_head = self.copyNext(head, relation_map)
        new_head = self.copyRandom(head, new_head, relation_map)
        return new_head

    def copyNext(self, head, relation_map):
        new_cur, cur = None, head
        while cur:
            new_node = Node(cur.val)
            relation_map[id(cur)] = new_node
            if new_cur is None:
                new_head = new_node
            else:
                new_cur.next = new_node
            new_cur = new_node
            cur = cur.next
        return new_head

    def copyRandom(self, head, new_head, relation_map):
        cur, new_cur = head, new_head
        while cur:
            if cur.random is None:
                new_cur.random = None
            else:
                new_cur.random = relation_map[id(cur.random)]
            cur = cur.next
            new_cur = new_cur.next
        return new_head



if __name__ == '__main__':
    pass
