from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        if len(nums) < k:
            return [max(nums)]
        nums = [-v for v in nums]
        the_heap = nums[:k]
        heapq.heapify(the_heap)
        ret = [-the_heap[0]]
        for i, value in enumerate(nums[k:], 1):
            the_heap.remove(nums[i-1])
            heapq.heapify(the_heap)
            heapq.heappush(the_heap, value)
            ret.append(-the_heap[0])

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([1, -1], 1))
