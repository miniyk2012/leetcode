from leetcode_projects.tree import TreeNode


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        node = root
        while node:
            pre = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if val < pre.val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)
        return root
