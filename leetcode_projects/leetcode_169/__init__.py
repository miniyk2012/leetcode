from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stats = defaultdict(int)
        length = len(nums)
        max_val = None
        count = None
        for val in nums:
            if not max_val:
                max_val = val
                count = 1
            stats[val] += 1
            if stats[val] > length / 2:
                return val
            if stats[val] > count:
                count = stats[val]
                max_val = val

        return max_val


if __name__ == '__main__':
    s = Solution()
    ret = s.majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(ret)
