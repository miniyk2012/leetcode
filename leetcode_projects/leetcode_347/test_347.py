import pytest

from leetcode_projects.leetcode_347.solution import Solution


def generate_cases():
    return [
        [[1, 1, 1, 2, 2, 3], 2, [1, 2]],
        [[1], 1, [1]],
        [[1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]]
    ]


@pytest.mark.parametrize("nums, k, expected", generate_cases())
def test_basic(nums, k, expected):
    solution = Solution()
    assert sorted(solution.topKFrequent(nums, k)) == sorted(expected)
