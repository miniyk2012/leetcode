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

    def findKthNumber1(self, n: int, k: int) -> int:
        """额, 还是超时"""
        self.total = 0
        self.ret = None
        for i in range(1, 10):
            self.dfs(0, i, n, k)
        return self.ret

    def dfs(self, prefix, i, n, k):
        cur = prefix * 10 + i
        if cur > n:
            return
        self.total += 1
        if self.total == k:
            self.ret = cur
            return
        for sub in range(0, 10):
            self.dfs(cur, sub, n, k)


    def findKthNumber(self, n: int, k: int) -> int:
        """前缀树有优化空间, 比如可以直接算出前面几颗树有多少节点"""
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(13, 10))
    # print(s.findKthNumber(2, 2))
