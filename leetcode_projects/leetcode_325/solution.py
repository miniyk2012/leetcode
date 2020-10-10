from typing import List


class Solution:
    """灵感来自花花的longest substring of XXX的模板
    https://zxi.mytechroad.com/blog/hashtable/leetcode-1542-find-longest-awesome-substring/"""

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        idx = dict()
        idx[0] = -1
        s = 0  # 初始状态, 表示前缀数组的和
        ans = 0
        for i, num in enumerate(nums):
            s += num
            if s - k in idx:
                ans = max(ans, i - idx[s - k])
            if s not in idx:
                idx[s] = i
        return ans


if __name__ == '__main__':
    nums = [1, -1, 5, -2, 3]
    k = 3
    s = Solution()
    assert s.maxSubArrayLen(nums, k) == 4

    nums = [-2, -1, 2, 1]
    k = 1
    assert s.maxSubArrayLen(nums, k) == 2
