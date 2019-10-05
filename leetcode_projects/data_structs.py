from __future__ import annotations
from typing import List, Callable, Optional
from numbers import Real


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


class SegmentTreeNode:

    def __init__(self, start: int, end: int, val: Real, left: SegmentTreeNode = None, right: SegmentTreeNode = None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right


OptionalSegmentTreeNode = Optional[SegmentTreeNode]


class SegmentTree:
    def __init__(self, nums: List[Real], metric: Callable[[Real, Real], Real]):
        self._nums = nums
        self._metric = metric
        if nums:
            self._root = self._buildTree(0, len(nums) - 1)

    def updateTree(self, index: int, val: Real) -> None:
        self._updateTree(self._root, index, val)

    def rangeQuery(self, i: int, j: int) -> Real:
        return self._rangeQuery(self._root, i, j)

    def _rangeQuery(self, node: OptionalSegmentTreeNode, i: int, j: int) -> Real:
        if node is None:
            raise RuntimeError("index outside array")
        if i == node.start and j == node.end:
            return node.val
        mid = node.start + (node.end - node.start) // 2
        if j <= mid:
            return self._rangeQuery(node.left, i, j)
        elif i > mid:
            return self._rangeQuery(node.right, i, j)
        else:
            return self._metric(self._rangeQuery(node.left, i, mid), self._rangeQuery(node.right, mid + 1, j))

    def _buildTree(self, start: int, end: int) -> SegmentTreeNode:
        if start == end:
            return SegmentTreeNode(start, end, self._nums[start])
        mid = start + (end - start) // 2
        left = self._buildTree(start, mid)
        right = self._buildTree(mid + 1, end)
        return SegmentTreeNode(start, end, self._metric(left.val, right.val), left, right)

    def _updateTree(self, node: OptionalSegmentTreeNode, index: int, val: Real) -> None:
        if node is None:
            raise RuntimeError("index outside array")
        if index == node.start == node.end:
            self._nums[index] = val
            node.val = val
            return
        mid = node.start + (node.end - node.start) // 2
        if index <= mid:
            self._updateTree(node.left, index, val)
        else:
            self._updateTree(node.right, index, val)
        assert node.left and node.right
        node.val = self._metric(node.left.val, node.right.val)
