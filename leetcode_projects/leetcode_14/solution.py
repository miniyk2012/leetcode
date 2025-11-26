from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(len(s) for s in strs)
        ret = ""
        for i in range(min_length + 1):
            pre = None
            equal = True
            for s in strs:
                if pre is None:
                    pre = s[:i]
                if pre != s[:i]:
                    equal = False
                    break
                pre = s[:i]
            if equal:
                ret = s[:i]
            else:
                return ret
        return ret
