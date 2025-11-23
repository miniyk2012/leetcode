import pytest

from leetcode_projects.leetcode_739.solution import Solution


def generate_cases():
    return [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
    ]


class TestDailyTemperatures:

    @pytest.mark.parametrize("temperatures, expected", generate_cases())
    def test_basic(self, temperatures, expected):
        solution = Solution()
        assert solution.dailyTemperatures(temperatures) == expected
        return
