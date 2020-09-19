from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.sum_left(root.left, True) + self.sum_left(root.right, False)

    def sum_left(self, node, left=True):
        if not node:
            return 0
        if not (node.left or node.right):
            if left:
                return node.val
            else:
                return 0
        return self.sum_left(node.left, True) + self.sum_left(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        isNodeLeaf = lambda node: not node.left and not node.right

        def dfs(node) -> int:
            ans = 0
            if node.left:
                ans += node.left.val if isNodeLeaf(node.left) else dfs(node.left)
            if node.right:
                ans += dfs(node.right) if not isNodeLeaf(node.right) else 0
            return ans

        return dfs(root) if root else 0

if __name__ == '__main__':
    s = Solution()
    l = [3, 9, 20, None, None, 15, 7]
    root = construct_tree(l)
    print(s.sumOfLeftLeaves(root))