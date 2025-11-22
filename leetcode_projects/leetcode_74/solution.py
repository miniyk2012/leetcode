from typing import List


class Solution:
    def searchM(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """2次二分查找, 我觉得更自然
        先查每列的首元素, 定位到某一行
        再查这一行里的元素
        """

        def find_row(row):
            start, end = 0, n-1
            while start <= end:
                mid = (start + end) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return False

        m = len(matrix)
        n = len(matrix[0])
        start_row, end_row = 0, m - 1
        while start_row <= end_row:
            mid_row = (start_row + end_row) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                if mid_row == m-1 or matrix[mid_row+1][0] > target:
                    return find_row(mid_row)
                else:
                    start_row = mid_row + 1
            else:
                if mid_row == 0:
                    return False
                else:
                    end_row = mid_row - 1
        return False

