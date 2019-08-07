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