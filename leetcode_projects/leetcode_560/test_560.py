import pytest

from leetcode_projects.leetcode_560.solution import Solution


class TestSubarraySum:
    @pytest.mark.parametrize("nums, k, expected", [
        # Typical mixed array
        ([1,1,1],2, 2),
        ([1,2,3], 3, 2),
        ([0,0,0], 1, 0),
        ([0,0,0], 0, 6),
        ([4], 4, 1),
    ])
    def test_basic(self, nums, k, expected):
        solution = Solution()
        ret = solution.subarraySum(nums, k)
        assert ret == expected