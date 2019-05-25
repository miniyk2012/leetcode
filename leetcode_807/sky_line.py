"""
https://www.bilibili.com/video/av44039304
https://leetcode.com/problems/max-increase-to-keep-city-skyline/submissions/
https://www.bilibili.com/video/av44039304
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total = 0
        row_num = len(grid)
        column_num = len(grid[0])
        max_along_column = [max(column) for column in zip(*grid)]
        max_along_row = [max(row) for row in grid]
        for i in range(row_num):
            for j in range(column_num):
                total += (min(max_along_row[i], max_along_column[j]) - grid[i][j])
        return total



def case1():
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    s = Solution()
    assert s.maxIncreaseKeepingSkyline(grid) == 35


if __name__ == '__main__':
    case1()
