from leetcode_projects.tree import TreeNode, construct_tree


class Solution:

    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self._l = 0
        self._r = 0
        self._cal_children(root, x)
        p = n - self._l - self._r - 1
        return max(p, self._l, self._r) > n // 2

    def _cal_children(self, root: TreeNode, x):
        if root is None:
            return 0
        l = self._cal_children(root.left, x)
        r = self._cal_children(root.right, x)
        if root.val == x:
            self._l, self._r = l, r
        return l + r + 1


def test():
    tree1 = construct_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    s = Solution()
    assert s.btreeGameWinningMove(tree1, 11, 3)
    tree2 = construct_tree([1, 2, 3, 4, 5])
    assert not s.btreeGameWinningMove(tree2, 5, 2)


if __name__ == '__main__':
    test()
