"""
https://leetcode-cn.com/problems/same-tree/
https://leetcode.com/problems/same-tree/submissions/
https://www.bilibili.com/video/av42885572
https://github.com/CreatCodeBuild/leetcode-solutions/blob/master/Python3/100_Same_Tree.py
"""

from typing import List


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ip = self.iterate(p)
        iq = self.iterate(q)
        p_node: TreeNode
        q_node: TreeNode
        for p_node in ip:
            try:
                q_node = next(iq)
            except StopIteration:
                return False
            both_true = False
            if p_node and q_node:
                both_true = True
                if p_node.val != q_node.val:
                    return False
            if not both_true and (p_node or q_node):
                return False
        try:
            next(iq)
        except StopIteration:
            return True
        else:
            return False

    @staticmethod
    def iterate(t: TreeNode):
        if t is None:
            raise StopIteration
        q: List[TreeNode] = [t]
        while q:
            ret: TreeNode = q.pop(0)
            yield ret
            if ret:
                q.append(ret.left)
                q.append(ret.right)
