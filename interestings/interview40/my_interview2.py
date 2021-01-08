from random import randint


class Solution:

    def solve(self, nums):
        result = []
        the_map = dict.fromkeys(nums, True)
        nums = sorted(nums)
        for idx1, a in enumerate(nums):
            for idx2 in range(idx1+1, len(nums)):
                b = nums[idx2]
                if -(a + b) in the_map and -(a+b) > b:
                    result.append((a, b, -a-b))

        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4, -3, -4]
    s = Solution()

    ret = s.solve(nums)
    print(ret)
