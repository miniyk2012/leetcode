from typing import List

from leetcode_projects.data_structs import FenwickTree


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = FenwickTree(len(nums))
        for i, val in enumerate(nums):
            self.tree.update(i + 1, val)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.query(j + 1) - self.tree.query(i)


def test():
    nums = [1, 3, 5]
    obj = NumArray(nums)
    assert obj.sumRange(0, 2) == 9
    obj.update(1, 2)
    assert obj.sumRange(0, 2) == 8


if __name__ == '__main__':
    test()
