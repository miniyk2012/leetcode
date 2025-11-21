from typing import List

import pytest

from leetcode_projects.leetcode_15.solution import Solution


class TestThreeSum:
    @pytest.mark.parametrize("nums, expected", [
        # Typical mixed array
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # Multiple triplets with no duplicates
        ([3, -2, 1, 0, -1, 2, -1, -4, 2], [[-2, -1, 3], [-2, 0, 2], [-1, -1, 2], [-1, 0, 1], [-4, 1, 3], [-4, 2, 2]]),
        # No solution returns empty
        ([1, 2, 3, 4, 5], []),
        # With duplicates in input
        ([-1, -1, -1, 2, 2], [[-1, -1, 2]]),
        # All zeros returns single triplet
        ([0, 0, 0, 0, 0], [[0, 0, 0]]),
    ])
    def test_three_sum_with_expected_results(self, nums, expected):
        sol = Solution()
        result = sol.threeSum(nums)

        # Normalize for comparison: sort inner lists and outer list
        normalized_result = sorted([sorted(t) for t in result]) if result is not None else []
        normalized_expected = sorted([sorted(t) for t in expected])

        assert normalized_result == normalized_expected

        # Ensure no duplicates in result
        if result:
            assert len(normalized_result) == len(set(tuple(t) for t in normalized_result))

    @pytest.mark.parametrize("nums", [
        [],
        [0],
        [1, -1],
    ])
    def test_three_sum_input_too_short_returns_empty(self, nums):
        sol = Solution()
        assert sol.threeSum(nums) == []

