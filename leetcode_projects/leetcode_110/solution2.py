from leetcode_projects.tree import TreeNode


class Solution:
    """自底向上, 后序遍历, 剪枝"""

    def recur(self, node):
        if not node:
            return 0
        left_depth = self.recur(node.left)
        if left_depth == -1:
            return -1
        right_depth = self.recur(node.right)
        if right_depth == -1:
            return -1
        if abs(left_depth - right_depth) > 1:
            return -1
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != - 1
