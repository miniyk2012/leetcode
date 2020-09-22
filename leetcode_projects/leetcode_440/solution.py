import heapq


class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)

    def __repr__(self): return str(self.val)


class Solution:
    def findKthNumber2(self, n: int, k: int) -> int:
        """速度太慢了"""
        k_heap = []
        for i in range(1, n + 1):
            str_i = MaxHeapObj(str(i))
            if len(k_heap) < k:
                heapq.heappush(k_heap, str_i)
            elif str_i > k_heap[0]:
                heapq.heappop(k_heap)
                heapq.heappush(k_heap, str_i)
        return k_heap[0]

    def findKthNumber(self, n: int, k: int) -> int:
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(13, 2))
