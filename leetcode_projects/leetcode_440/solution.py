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
        """前缀树有优化空间, 可以直接得出某棵前缀树里面小于等于n的节点数"""

        def get_count(prefix, n):
            """某棵前缀树里面小于等于n的节点数"""
            cnt = 0
            a, b = prefix, prefix + 1
            while a <= n:
                cnt += min(b, n + 1) - a
                a *= 10
                b *= 10
            return cnt

        # 逐步扩充前缀树, 找到最终结果
        prefix = 1
        p = 1  # 当前的前缀树的排名
        while p < k:
            cnt = get_count(prefix, n)
            if cnt + p <= k:
                prefix += 1  # 位置往右移动, 排名增加左边的那颗前缀树中所有节点
                p += cnt
            else:
                prefix *= 10
                p += 1  # 位置往下移动, 排名+1
        return prefix


if __name__ == '__main__':
    s = Solution()
    print(s.findKthNumber(13, 2))
    print(s.findKthNumber(10, 3))
    print(s.findKthNumber2(10, 3))
