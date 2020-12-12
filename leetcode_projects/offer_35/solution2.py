# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        cur = head
        new_head = None
        while cur:
            if not new_head:
                new_head = self.get_new_node(visited, cur)
                new_cur = new_head
            new_cur.next = self.get_new_node(visited, cur.next)
            new_cur.random = self.get_new_node(visited, cur.random)
            new_cur = new_cur.next
            cur = cur.next
        return new_head

    def get_new_node(self, visited, old_node):
        if old_node is None:
            return None
        if old_node in visited:
            return visited[old_node]
        new_node = Node(old_node.val, None, None)
        visited[old_node] = new_node
        return new_node
