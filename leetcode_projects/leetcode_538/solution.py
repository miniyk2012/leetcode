from leetcode_projects.tree import TreeNode, construct_tree, bfs_visit_tree


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.inorder(root, 0)
        return root

    def inorder(self, root, summary):
        if root.right:
            summary = self.inorder(root.right, summary)
        root.val = root.val + summary
        summary = root.val
        if root.left:
            summary = self.inorder(root.left, root.val)
        return summary


if __name__ == '__main__':
    s = Solution()
    l = [5, 2, 13]
    root = construct_tree(l)
    root = s.convertBST(root)
    print(bfs_visit_tree(root))