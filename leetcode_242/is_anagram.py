class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}
        for c in s:
            m1[c] = m1.get(c, 0) + 1
        for c in t:
            m2[c] = m2.get(c, 0) + 1
        return m1 == m2

    def isAnagram3(self, s: str, t: str) -> bool:
        l1, l2 = [0] * 26, [0] * 26
        for c in s:
            l1[ord(c) - ord('a')] += 1
        for c in t:
            l2[ord(c) - ord('a')] += 1
        return l1 == l2
