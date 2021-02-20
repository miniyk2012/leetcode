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
        if not root:
            return self.result
        self.traverse(root)
        return self.result

    def traverse(self, node: 'Node'):
        self.result.append(node.val)
        for x in node.children:
            self.traverse(x)
