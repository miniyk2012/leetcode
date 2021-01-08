from leetcode_projects.tree import TreeNode


class Solution:
    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)