from typing import List


class Solution:
    """不同路径"""

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        diff_paths = [[0] * (n + 1) for _ in range(m + 1)]
        diff_paths[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    diff_paths[i][j] = 0
                else:
                    diff_paths[i][j] += diff_paths[i][j - 1] + diff_paths[i - 1][j]
        return diff_paths[m][n]


def test():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    s = Solution()
    assert s.uniquePathsWithObstacles(grid) == 2


if __name__ == '__main__':
    test()
