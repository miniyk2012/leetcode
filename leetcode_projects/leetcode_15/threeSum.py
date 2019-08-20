from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = list(sorted(nums))
        ret = []
        pre = None
        for i, num in enumerate(nums):
            if num == pre:
                continue
            memo = {}
            left_nums = nums[i + 1:]
            total = 0 - num
            repeat = set()
            for val in left_nums:
                if (total - val) in memo:
                    if (total - val, val) not in repeat:
                        repeat.add((total - val, val))
                        ret.append([num, total - val, val])
                else:
                    memo[val] = True
            pre = num

        return ret

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = list(sorted(nums))
        ret = set()
        for i, num in enumerate(nums):
            if i > 1 and num == nums[i - 1]:
                continue
            memo = {}
            left_nums = nums[i + 1:]
            total = 0 - num
            for val in left_nums:
                if (total - val) in memo:
                    ret.add((num, total - val, val))
                else:
                    memo[val] = True

        return list(map(list, ret))


if __name__ == '__main__':
    s = Solution()
    ret = s.threeSum2([-1, 0, 1, 2, -1, -4])
    print(ret)
    ret = s.threeSum2([0, 0, 0, 0])
    print(ret)
