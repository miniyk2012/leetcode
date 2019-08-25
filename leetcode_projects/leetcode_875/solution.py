import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        r = max(piles) + 1
        l = 1
        while l < r:
            m = r + (l - r) // 2
            spend_time = sum(math.ceil(num / m) for num in piles)
            if spend_time > H:
                l = m + 1
            else:
                r = m
        return l  # 返回的是使得spend_time<=H的最小的吃香蕉速度


def test():
    s = Solution()
    piles = [3, 6, 7, 11]
    H = 8
    assert s.minEatingSpeed(piles, H) == 4

    piles = [30, 11, 23, 4, 20]
    H = 5
    assert s.minEatingSpeed(piles, H) == 30

    piles = [30, 11, 23, 4, 20]
    H = 6
    assert s.minEatingSpeed(piles, H) == 23


if __name__ == "__main__":
    test()
