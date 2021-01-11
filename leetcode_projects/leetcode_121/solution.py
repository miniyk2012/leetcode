from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        p = 0  # 第i天的最大收益
        l = prices[0]
        for i in range(1, len(prices)):
            l = min(l, prices[i])
            p = max(p, prices[i] - l)
        return p


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    ret = s.maxProfit(prices)
    assert ret == 5

    prices = [7, 6, 4, 3, 1]
    ret = s.maxProfit(prices)
    assert ret == 0
