"""
https://leetcode-cn.com/problems/same-tree/
https://leetcode.com/problems/same-tree/submissions/
https://www.bilibili.com/video/av42885572
https://github.com/CreatCodeBuild/leetcode-solutions/blob/master/Python3/100_Same_Tree.py
"""

from typing import List
from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ip = self.iterate(p)
        iq = self.iterate(q)
        for p_val in ip:
            try:
                q_val = next(iq)
            except StopIteration:
                return False
            if p_val != q_val:
                return False
        try:
            next(iq)
        except StopIteration:
            return True
        return False

    @staticmethod
    def iterate(t: TreeNode):
        if t is None:
            raise StopIteration
        q: List[TreeNode] = [t]
        while q:
            ret: TreeNode = q.pop(0)
            if ret:
                yield ret.val
            else:
                yield None
            if ret:
                q.append(ret.left)
                q.append(ret.right)


def test_same_tree():
    l1 = [1, 2, 4]
    l2 = [1, 2, 3, None, 4, 5, 6]
    t1 = construct_tree(l1)
    t2 = construct_tree(l2)
    s = Solution()
    print()
    for i in s.iterate(t1):
        print(i, end=' ')
    print()
    for i in s.iterate(t2):
        print(i, end=' ')
