from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        self._n = len(nums)
        self._nums = nums
        self._m = m
        self._dp = []

        self.init_dp()
        self.do_dp()
        return self._dp[self._m][self._n]

    def init_dp(self):
        for j in range(self._m + 1):
            self._dp.append([0] * (self._n + 1))

    def do_dp(self):
        dp = self._dp
        nums = self._nums
        cur_sum = 0
        for j in range(0, self._m):
            for i in range(self._n):
                if j == 0:
                    dp[j + 1][i + 1] = dp[j + 1][i] + nums[i]
                else:
                    # nums[i]独自一组
                    dp1 = max(dp[j][i], nums[i])

                    # nums[i]与前面连在一起
                    dp2 = max(dp[j + 1][i], cur_sum + nums[i])

                    dp[j + 1][i + 1] = min(dp1, dp2)

                    if dp1 < dp2:
                        cur_sum = nums[i]
                    else:
                        cur_sum = cur_sum + nums[i]


def test():
    nums = [10]
    m = 1
    s = Solution()
    assert s.splitArray(nums, m) == 10

    nums = [7, 2, 5, 10, 8]
    m = 2
    s = Solution()
    assert s.splitArray(nums, m) == 18

    nums = [1, 2, 3, 4, 7, 2, 5, 10, 8]
    m = 4
    s = Solution()
    assert s.splitArray(nums, m) == 14

    nums = [5, 10, 6]
    m = 2
    assert s.splitArray(nums, m) == 15

    nums = [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]
    m = 8
    s = Solution()
    assert s.splitArray(nums, m) == 25


if __name__ == '__main__':
    test()
