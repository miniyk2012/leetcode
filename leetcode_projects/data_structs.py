from typing import List


class UnionFindSet:
    """并查集类, 只支持所有元素都是整数.
    如果要支持非整数的元素请不要修改该类, 可以通过映射的方式扩展功能"""

    def __init__(self, n: int):
        """支持的元素为0~n-1
        :param n: 最多元素个数
        """
        self._parents: List[int] = [i for i in range(n)]  # _parents[u] = v 表示u的父亲是v
        self._ranks: List[int] = [1] * n  # _ranks[find(u)] = v 表示u所在的连通集rank为v

    def find(self, u: int) -> int:
        """返回num所在连通集的根,
        在遍历的同时make tree flat"""
        if self._parents[u] != u:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]

    def union(self, u: int, v: int) -> None:
        """合并u, v所在的连通集"""
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        rank_u, rank_v = self._ranks[root_u], self._ranks[root_v]
        if rank_u > rank_v:
            self._parents[root_v] = root_u
        elif rank_u < rank_v:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] = rank_v + 1


class FenwickTree:
    """该数据结构用来计算数组一个连续区间数字之和，且数组中的数字可变。
    也叫Binary Indexed Tree
    """

    def __init__(self, n):
        """从下标1开始, 下标0无用"""
        self._sum = [0 for _ in range(n + 1)]

    def query(self, i):
        """查询得到第1个元素~第i个元素的和"""
        s = 0
        while i > 0:
            s += self._sum[i]
            i -= i & (-i)
        return s

    def update(self, i, delta):
        """这个update更新的是与旧值相比的变化值，当心"""
        while i < len(self._sum):
            self._sum[i] += delta
            i += i & (-i)
