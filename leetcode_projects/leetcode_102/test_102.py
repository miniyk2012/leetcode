from leetcode_projects.leetcode_102.solution import Solution
from leetcode_projects.tree import construct_tree


def test_basic():
    tree = construct_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    assert s.levelOrder(tree) == [[3],[9,20],[15,7]]