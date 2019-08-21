# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version < 4:
        return False
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n + 1
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


def test():
    s = Solution()
    assert s.firstBadVersion(100) == 4
    assert s.firstBadVersion(4) == 4


if __name__ == '__main__':
    test()
