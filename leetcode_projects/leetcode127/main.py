from typing import List


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """暴力迭代"""
        most_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                diff = prices[j] - prices[i]
                if diff > most_profit:
                    most_profit = diff

        return most_profit

    def maxProfit2(self, prices: List[int]) -> int:
        minValue = float('inf')
        most_profit = 0
        for v in prices:
            if v < minValue:
                minValue = v
            if v - minValue > most_profit:
                most_profit = v - minValue
        return most_profit

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [0] * len(prices)  # dp[i]到第i天为止, 能赚的最多的钱
        minValue = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minValue:
                minValue = prices[i]
            if prices[i] - minValue > dp[i - 1]:
                dp[i] = prices[i] - minValue
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    assert 5 == s.maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == s.maxProfit([7, 6, 4, 3, 1])
    assert 1 == s.maxProfit([1, 2])
