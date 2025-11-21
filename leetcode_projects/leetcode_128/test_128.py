import pytest

from leetcode_projects.leetcode_128.solution import Solution

def generate_testcases():
    return [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([1,2,0,1], 3),
        ([9,1,4,7,3,-1,0,5,8,-1,6,-1,2], 11),
        ([1,3,5,2,4], 5),
        ([9,1,-3,2,4,8,3,-1,6,-2,-4,7], 4)
    ]


@pytest.mark.parametrize("input_data,expected", generate_testcases())
def test_128(input_data, expected):
    result = Solution().longestConsecutive(input_data)
    assert result == expected
