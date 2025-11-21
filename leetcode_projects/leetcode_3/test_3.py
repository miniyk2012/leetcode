import pytest

from leetcode_projects.leetcode_3.solution import Solution


class TestLongestSubStr:

    @pytest.mark.parametrize("s, sub_len", [
        ["abcabcbb", 3],
        ["bbbbb", 1],
        ["pwwkew", 3],
        ["b", 1],
        ["", 0],
        ["au", 2],
        ["auw", 3],
    ])
    def test_case(self, s, sub_len):
        solution = Solution()
        assert solution.lengthOfLongestSubstring(s) == sub_len
