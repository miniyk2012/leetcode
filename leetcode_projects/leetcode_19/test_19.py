import pytest

from leetcode_projects.leetcode_19.solution import Solution
from leetcode_projects.tree import construct_list, destruct_listnode


def print_l(l):
    while l:
        print(l.val, end=' ')
        l = l.next
    print()


@pytest.mark.parametrize("arr, n, expected", [
    [[1, 2, 3, 4, 5], 2, [1, 2, 3, 5]],
    [[1], 1, []],
    [[1, 2], 1, [1]]
])
def test_basic(arr, n, expected):
    l = construct_list(arr)
    solution = Solution()
    ret = solution.removeNthFromEnd(l, n)
    assert destruct_listnode(ret) == expected
