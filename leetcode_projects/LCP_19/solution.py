class Solution:
    def minimumOperations(self, leaves: str) -> int:
        # 动态规划解决该问题
        dp = [
            [0] * len(leaves),  # d[0][i]到第i个时, 全红最少改动几次
            [0] * len(leaves),  # d[1][i]到第i个时, 先红再黄最少改动几次
            [0] * len(leaves),  # d[2][i]到第i个时, 先红再黄再红最少改动几次
        ]
        # 最终结果是d[2][-1]
        for i in range(len(leaves)):
            if i < 1:
                dp[0][i] = 1 if leaves[0] == 'y' else 0
            else:
                dp[0][i] = dp[0][i - 1] + (1 if leaves[i] == 'y' else 0)
            if i < 1:
                dp[1][i] = dp[0][i]
            else:
                dp[1][i] = min(
                    dp[0][i - 1] + (1 if leaves[i] == 'r' else 0),
                    dp[1][i - 1] + (1 if leaves[i] == 'r' else 0)
                )
            if i < 2:
                dp[2][i] = dp[1][i]  # 边界条件很巧妙
            else:
                dp[2][i] = min(
                    dp[1][i - 1] + (1 if leaves[i] == 'y' else 0),
                    dp[2][i - 1] + (1 if leaves[i] == 'y' else 0),
                )
        return dp[2][-1]


if __name__ == '__main__':
    s = Solution()
    leaves = "rrryyyrryyyrr"
    assert s.minimumOperations(leaves) == 2

    leaves = "ryr"
    assert s.minimumOperations(leaves) == 0
