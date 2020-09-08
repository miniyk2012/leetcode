from typing import List
from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """C(n,k)"""
        self.rets = []
        remain = list(range(1, n + 1))
        self.combine_remain([], remain, n, k)
        return self.rets

    def combine_remain(self, ret, remain, n, k):
        if k == 0:
            self.rets.append(ret[:])
            return
        for i, v in enumerate(remain[:n-k+1]):
            ret.append(v)
            self.combine_remain(ret, remain[i + 1:], n, k - 1)
            ret.pop(-1)


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
    print(s.combine(5, 2))
    print(s.combine(5, 1))
    print(s.combine(5, 4))
    print(s.combine(5, 5))
    print(s.combine(1, 0))
