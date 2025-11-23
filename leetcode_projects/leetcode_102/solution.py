# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from leetcode_projects.tree import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret
        q = [root]
        while q:
            num = len(q)
            ret.append(list(map(lambda x: x.val, q)))
            for node in q[:]:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            q = q[num:]
        return ret



