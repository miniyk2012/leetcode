# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children: List['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    """迭代实现前序遍历"""

    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            tail = stack.pop()
            result.append(tail.val)
            stack.extend(tail.children[::-1])

        return result
