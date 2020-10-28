from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        values = []
        for row in grid:
            values.append([0] * len(row))
        values[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i > 0 and j > 0:
                    values[i][j] = max(values[i - 1][j], values[i][j - 1]) + grid[i][j]
                elif i == 0:
                    values[i][j] = values[i][j - 1] + grid[i][j]
                else:
                    values[i][j] = values[i - 1][j] + grid[i][j]
        return values[-1][-1]


if __name__ == '__main__':
    s = Solution()
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    result = s.maxValue(grid)
    print(result)
