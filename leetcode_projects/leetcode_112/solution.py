from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:  # 到叶子节点的时候再做判断
            return root.val == sum

        l = self.hasPathSum(root.left, sum - root.val)
        r = self.hasPathSum(root.right, sum - root.val)
        return l or r


def test_has_pathsum():
    nums = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = construct_tree(nums)
    s = Solution()
    assert s.hasPathSum(root, 22)

    nums = [1, 2]
    root = construct_tree(nums)
    assert not s.hasPathSum(root, 1)

    nums = [1, -2, -3, 1, 3, -2, None, -1]
    root = construct_tree(nums)
    assert s.hasPathSum(root, -1)
