from tree import TreeNode
from tree import construct_tree


class Solution:
    a_sum = 0

    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        self.L, self.R = L, R
        self.visit1(root)
        return self.a_sum

    def visit1(self, node: TreeNode) -> None:
        if node is None:
            return
        if node.val < self.L:
            self.visit1(node.right)
            return
        if node.val > self.R:
            self.visit1(node.left)
            return
        self.visit1(node.left)
        self.visit1(node.right)
        self.a_sum += node.val

    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        self.L, self.R = L, R
        self.visit2(root)
        return self.a_sum

    def visit2(self, node: TreeNode) -> None:
        if self.L <= node.val <= self.R:
            self.a_sum += node.val
        if node.val > self.L and node.left:
            self.visit2(node.left)
        if node.val < self.R and node.right:
            self.visit2(node.right)

    def rangeSumBST3(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if L <= node.val <= R:
                ans += node.val
            if node.val > L and node.left:
                stack.append(node.left)
            if node.val < R and node.right:
                stack.append(node.right)
        return ans


def test1():
    l = [10, 5, 15, 3, 7, None, 18]
    tree = construct_tree(l)
    s = Solution()
    a_sum = s.rangeSumBST1(tree, 7, 15)
    assert a_sum == 32


def test2():
    l = [10, 5, 15, 3, 7, None, 18]
    tree = construct_tree(l)
    s = Solution()
    a_sum = s.rangeSumBST2(tree, 7, 15)
    assert a_sum == 32


def test3():
    l = [10, 5, 15, 3, 7, None, 18]
    tree = construct_tree(l)
    s = Solution()
    a_sum = s.rangeSumBST3(tree, 7, 15)
    assert a_sum == 32
