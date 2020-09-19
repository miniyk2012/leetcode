from typing import List

from leetcode_projects.tree import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pass


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    tree = s.buildTree(preorder, inorder)