from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0:
            return 1 + r
        if r == 0:
            return 1 + l
        return min(l, r) + 1


if __name__ == '__main__':
    tree = construct_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    assert s.minDepth(tree) == 2
    tree = construct_tree([1, 2])
    assert s.minDepth(tree) == 2
