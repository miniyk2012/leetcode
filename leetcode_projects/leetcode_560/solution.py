from typing import List


class Solution:
    """和为K的子数组"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        ret = 0
        total = 0
        length = len(nums)
        memo = {}
        for i in range(0, length):
            total = total + nums[i]
            print(total, memo)
            if total in memo:
                ret += 1
            else:
                memo[k+nums[i]] = True
        return ret

        return 0
    def subarraySum_slow(self, nums: List[int], k: int) -> int:
        ret = 0
        length = len(nums)
        pre_sum = [0 for _ in range(0, length+1)]
        for i in range(1, length+1):
            pre_sum[i] = nums[i-1] + pre_sum[i - 1]
        for i in range(0, length):
            for j in range(i, length):
                if pre_sum[j+1] - pre_sum[i] == k:
                    ret += 1
        return ret


    def subarraySum1(self, nums: List[int], k: int) -> int:
        idx = {0: 1}  # idx[s]= 满足前缀和为s的索引个数, 初始和为0的个数认为是1, 对从头开始的子数组较为方便
        ans = 0
        s = 0  # 前缀数组的和作为状态
        for i, num in enumerate(nums):
            s += num
            if s - k in idx:
                ans += idx[s - k]
            if s in idx:
                idx[s] += 1
            else:
                idx[s] = 1
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    s = Solution()
    assert s.subarraySum1(nums, k) == 2
