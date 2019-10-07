import pytest

from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False  # 提前短路
        ret1 = self.mirror(node1.left, node2.right)
        ret2 = self.mirror(node1.right, node2.left)
        return ret1 and ret2


@pytest.mark.parametrize('nums, expected',
                         [((1, 2, 2, 3, 4, 4, 3), True),
                          ((1, 2, 2, None, 3, None, 3), False)
                          ])
def test_symmetric(nums, expected):
    root = construct_tree(nums)
    s = Solution()
    assert s.isSymmetric(root) == expected
