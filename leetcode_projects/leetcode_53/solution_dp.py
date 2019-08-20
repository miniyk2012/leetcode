from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        dp_ending_here = [0] * nums_length
        dp_sofar = [0] * nums_length
        dp_ending_here[0] = dp_sofar[0] = nums[0]
        for i in range(1, nums_length):
            dp_ending_here[i] = max(dp_ending_here[i - 1] + nums[i], nums[i])
            dp_sofar[i] = max(dp_sofar[i - 1], dp_ending_here[i])
        return dp_sofar[nums_length - 1]


def test():
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert s.maxSubArray([8, -19, 5, -4, 20]) == 21


if __name__ == '__main__':
    test()
