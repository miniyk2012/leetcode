from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_path = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = min_path[i - 1][j] + grid[i - 1][j - 1]
                left = min_path[i][j - 1] + grid[i - 1][j - 1]
                if i == 1:
                    min_path[i][j] = left
                elif j == 1:
                    min_path[i][j] = up
                else:
                    min_path[i][j] = min(up, left)
        print(min_path)
        return min_path[m][n]


def test():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    assert Solution().minPathSum(grid) == 7


if __name__ == '__main__':
    test()
