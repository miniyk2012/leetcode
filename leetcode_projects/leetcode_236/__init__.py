from leetcode_projects.tree import TreeNode, construct_tree

memo = {}


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        if root.left and self.in_tree(root.left, p) and self.in_tree(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.right and self.in_tree(root.right, p) and self.in_tree(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def in_tree(self, node: TreeNode, v):
        if (node, v) in memo:
            return True
        if node is None:
            return False
        if self.in_tree(node.left, v):
            memo[(node, v)] = 1
            return True
        if node.val == v.val:
            memo[(node, v)] = 1
            return True
        if self.in_tree(node.right, v):
            memo[(node, v)] = 1
            return True
        return False

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            # assert (left is None and right is None)
            return root


if __name__ == '__main__':
    s = Solution()
    tree = construct_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    node = s.lowestCommonAncestor2(tree, TreeNode(5), TreeNode(1))
    print(node.val)
