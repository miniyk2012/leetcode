"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        head.prev = None
        return head

    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev
        tail = curr
        curr.prev = prev
        prev.next = curr
        # the curr.next would be tempered in the recursive function
        tempNext, child = curr.next, curr.child
        curr.child, curr.next = None, None
        if child:
            tail = self.flatten_dfs(curr, child)
        if tempNext:
            tail = self.flatten_dfs(tail, tempNext)
        return tail
