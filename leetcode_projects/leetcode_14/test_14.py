import pytest

from leetcode_projects.leetcode_14.solution import Solution


def generate_cases():
    return [
        (["dog", "racecar", "car"], ""),
        (["flower", "flow", "flight"], "fl"),
        (["a"], "a"),
    ]


@pytest.mark.parametrize("strs, expected", generate_cases())
def test_basic(strs, expected):
    solution = Solution()
    assert expected == solution.longestCommonPrefix(strs)
