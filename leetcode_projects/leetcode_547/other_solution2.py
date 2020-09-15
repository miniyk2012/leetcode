from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """审题有误, 看成矩阵是否连通了, 不过这个做法对错误审题是正确的"""
        self.group_id = 0
        self.M = M
        group_matrix = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                self.dfs_group(i, j, group_matrix, True)
        return self.group_id

    def dfs_group(self, i, j, group_matrix, new_visit):
        if i < 0 or i >= len(self.M):
            return
        if j < 0 or j >= len(self.M[0]):
            return
        positions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        if self.M[i][j] == 0:
            return
        if group_matrix[i][j] != 0:
            return
        if new_visit:
            self.group_id += 1
        group_matrix[i][j] = self.group_id
        for position in positions:
            m, n = i + position[0], j + position[1]
            self.dfs_group(m, n, group_matrix, False)


if __name__ == '__main__':
    s = Solution()
    m = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    print(s.findCircleNum(m))

    m = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    print(s.findCircleNum(m))

    m = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    print(s.findCircleNum(m))