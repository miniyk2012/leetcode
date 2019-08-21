import math


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x + 1
        while l < r:
            m = l + (r - l) // 2
            if m * m <= x:
                l = m + 1
            else:
                r = m
        # print(l - 1, x)
        return l - 1


def test():
    s = Solution()
    for i in range(1, 10000):
        assert s.mySqrt(i) == int(math.sqrt(i))


if __name__ == '__main__':
    test()
