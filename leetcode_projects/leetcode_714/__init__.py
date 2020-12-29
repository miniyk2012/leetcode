from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """
        dp[i][0]: 第i天交易完后手中没有股票时的最大收益
        dp[i][1]: 第i天交易完后手中有股票时的最大收益
        :param prices:
        :param fee:
        :return:
        """
        if not prices:
            return 0
        dp = []
        for _ in prices:
            dp.append([0, 0])
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)  # 卖出股票要收手续费
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])  # 买入股票
        return dp[-1][0]


if __name__ == '__main__':
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    s = Solution()
    assert s.maxProfit(prices, fee) == 8
