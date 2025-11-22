import pytest

from leetcode_projects.leetcode_74.solution import Solution


def generate_testcase():
    return [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True],
        [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False],
    ]


class TestSearchMatrix:


    @pytest.mark.parametrize("matrix, target, found", generate_testcase())
    def test_basic(self, matrix, target, found):
        solution = Solution()
        assert solution.searchMatrix(matrix, target) is found