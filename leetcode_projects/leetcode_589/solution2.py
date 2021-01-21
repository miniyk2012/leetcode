# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children: List['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    """递归实现前序遍历"""

    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        stack = []
        if not root:
            return self.result
        stack.append(root)
        while stack:
            tail = stack.pop()
            self.result.append(tail.val)
            for child in tail.children[::-1]:
                stack.append(child)

        return self.result
