from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == []:
            return []
        self.matrix = matrix
        self.rets = []
        self.order(0, len(matrix) - 1, 0, len(matrix[0]) - 1)
        return self.rets

    def order(self, row_start, row_end, col_start, col_end):
        if row_start == row_end:
            self.rets.extend(self.matrix[row_start][col_start:col_end + 1])
            return
        if col_start == col_end:
            for i in range(row_start, row_end + 1):
                self.rets.append(self.matrix[i][col_end])
            return
        self.rets.extend(self.matrix[row_start][col_start:col_end])
        for i in range(row_start, row_end):
            self.rets.append(self.matrix[i][col_end])
        self.rets.extend(self.matrix[row_end][col_end:col_start:-1])
        for i in range(row_end, row_start, -1):
            self.rets.append(self.matrix[i][col_start])
        if row_end - 1 < row_start + 1 or col_start + 1 > col_end - 1:
            return
        self.order(row_start + 1, row_end - 1, col_start + 1, col_end - 1)


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s = Solution()
    assert s.spiralOrder(m) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert s.spiralOrder(m) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
