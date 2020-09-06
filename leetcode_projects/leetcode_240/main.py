import bisect
from typing import List


class Solution:
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        """基本思想是二分法
        先决定哪些行可能包含, 然后每行再用二分法"""
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        first_column = [row[0] for row in matrix]
        last_column = [row[-1] for row in matrix]
        start_row = bisect.bisect_left(last_column, target)  # 左闭
        end_row = bisect.bisect(first_column, target)  # 右开
        for row in range(start_row, end_row):
            if self.contain(matrix[row], target):
                return True
        return False

    def contain(self, line, target):
        start, end = 0, len(line) - 1
        while start <= end:
            mid = (start + end) // 2
            mid_value = line[mid]
            if mid_value == target:
                return True
            elif mid_value < target:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """基本思想是二分法
        先决定哪些行可能包含, 然后每行再用二分法"""
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        first_column = [row[0] for row in matrix]
        last_column = [row[-1] for row in matrix]
        start_row = bisect.bisect_left(last_column, target)  # 左闭
        end_row = bisect.bisect(first_column, target)  # 右开
        for row in range(start_row, end_row):
            if self.contain(matrix[row], target):
                return True
        return False
        """其实有更快的方案
        从二维数组的右上角开始查找。如果当前元素等于目标值，则返回 true。
        如果当前元素大于目标值，则移到左边一列。如果当前元素小于目标值，则移到下边一行。"""
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        node = [0, len(matrix[0]) - 1]
        while node[0] < len(matrix) and node[1] >= 0:
            if matrix[node[0]][node[1]] < target:
                node[0] += 1
            elif matrix[node[0]][node[1]] > target:
                node[1] -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    s = Solution()
    print(s.searchMatrix(matrix, 5))
    print(s.searchMatrix(matrix, 20))

    print(s.searchMatrix([[-5]], -5))
