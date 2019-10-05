from __future__ import annotations

from typing import List

from leetcode_projects.data_structs import SegmentTree


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree: SegmentTree = SegmentTree(nums, lambda a, b: a + b)

    def update(self, i: int, val: int) -> None:
        self.tree.updateTree(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.rangeQuery(i, j)


def test():
    nums = [1, 3, 5]
    obj = NumArray(nums)
    assert obj.sumRange(0, 2) == 9
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8
