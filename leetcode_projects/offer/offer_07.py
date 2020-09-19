from typing import List

from leetcode_projects.tree import TreeNode, bfs_visit_tree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        if index > 0:
            left_inorder = inorder[0:index]
            left_preorder = preorder[1:index + 1]
            head.left = self.buildTree(left_preorder, left_inorder)
        if index < len(inorder) - 1:
            right_inorder = inorder[index + 1:]
            right_preorder = preorder[index + 1:]
            head.right = self.buildTree(right_preorder, right_inorder)
        return head


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    tree = s.buildTree(preorder, inorder)
    l = bfs_visit_tree(tree)
    print(l)

