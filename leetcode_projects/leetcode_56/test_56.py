from typing import List, Tuple
import pytest
from leetcode_projects.leetcode_56.solution_56 import Solution


def generate_testcases() -> List[Tuple[List[List[int]], List[List[int]]]]:
    return [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([], []),
        ([[4, 7], [1, 4]], [[1, 7]]),
    ]


@pytest.mark.parametrize("input_data,expected", generate_testcases())
def test_49(input_data, expected):
    solution = Solution()
    result = solution.merge(input_data)
    assert result == expected
