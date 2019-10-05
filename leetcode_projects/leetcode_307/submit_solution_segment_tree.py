from typing import List, Callable, Optional


class SegmentTreeNode:

    def __init__(self, start: int, end: int, val: int, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right


OptionalSegmentTreeNode = Optional[SegmentTreeNode]


class SegmentTree:
    def __init__(self, nums: List[int], metric: Callable[[int, int], int]):
        self._nums = nums
        self._metric = metric
        if nums:
            self._root = self._buildTree(0, len(nums) - 1)

    def updateTree(self, index: int, val: int) -> None:
        self._updateTree(self._root, index, val)

    def rangeQuery(self, i: int, j: int) -> int:
        return self._rangeQuery(self._root, i, j)

    def _rangeQuery(self, node: OptionalSegmentTreeNode, i: int, j: int) -> int:
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

    def _updateTree(self, node: OptionalSegmentTreeNode, index: int, val: int) -> None:
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
