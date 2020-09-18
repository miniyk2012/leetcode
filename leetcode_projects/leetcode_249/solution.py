from typing import List
from collections import defaultdict
from functools import reduce


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map_groups = defaultdict(list)
        for string in strings:
            if len(string) < 2:
                map_groups[len(string)].append(string)
            else:
                key = []
                a = string[0]
                for x in string[1:]:
                    key.append((ord(x) - ord(a)) % 26)
                    x = a
                key = tuple(key)
                map_groups[key].append(string)
        return list(map_groups.values())


if __name__ == '__main__':
    s = Solution()
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    print(s.groupStrings(strings))

    print((ord('a') - ord('z')) % 26)
    print((ord('b') - ord('a')) % 26)
