from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for letter in strs:
            v = ''.join(sorted(letter))
            groups[v].append(letter)
        return list(groups.values())
