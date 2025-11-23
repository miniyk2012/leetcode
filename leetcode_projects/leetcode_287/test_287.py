import pytest

from leetcode_projects.leetcode_287.solution import Solution


@pytest.mark.parametrize("nums, expected", [
    [[1,3,4,2,2], 2],
    [[3,1,3,4,2], 3],
    [[3,3,3,3,3], 3]
])
def test_basic(nums, expected):
    solution = Solution()
    assert solution.findDuplicate(nums) == expected
