from typing import List, Tuple

import pytest

from leetcode_projects.leetcode_11.solution import Solution


def generate_testcases() -> List[Tuple[List[int], int]]:
    return [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]


@pytest.mark.parametrize("input_data,expected", generate_testcases())
def test_11(input_data, expected):
    """Test LeetCode 11: Container With Most Water."""
    sol = Solution()
    result = sol.maxArea(input_data)
    assert result == expected
