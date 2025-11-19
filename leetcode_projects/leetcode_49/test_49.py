from typing import List, Tuple
import pytest
from leetcode_projects.leetcode_49.solution import Solution


def generate_testcases() -> List[Tuple[List[str], List[List[str]]]]:
    return [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]


@pytest.mark.parametrize("input_data,expected", generate_testcases())
def test_49(input_data, expected):
    solution = Solution()
    result = solution.groupAnagrams(input_data)
    assert sorted(sorted(v) for v in result) == sorted(sorted(v) for v in expected)