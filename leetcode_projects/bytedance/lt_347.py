from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """堆排序"""
        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1
        pq = []
        for num, count in count_map.items():
            if len(pq) == k:
                if pq[0][0] < count:
                    heapq.heappushpop(pq, (count, num))
            else:
                heapq.heappush(pq, (count, num))
        return [num for _, num in heapq.nlargest(k, pq)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """桶排序"""
        count_map = defaultdict(int)
        for i in nums:
            count_map[i] += 1
        bucket = [None] * (len(nums) + 1)
        for num, count in count_map.items():
            if bucket[count] is None:
                bucket[count] = [num]  # 小心频率一样的num
            else:
                bucket[count].append(num)
        i, ret = len(nums) - 1, []
        while len(ret) < k:
            if bucket[i]:
                ret.extend(bucket[i])
            i -= 1
        return ret


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    s = Solution()
    print(s.topKFrequent2(nums, k))
    nums = [1]
    k = 1
    print(s.topKFrequent2(nums, k))
    nums = [5, 3, 1, 1, 1, 3, 73, 1]
    print(s.topKFrequent2(nums, 2))
    nums = [1, 2]
    print(s.topKFrequent2(nums, 2))
