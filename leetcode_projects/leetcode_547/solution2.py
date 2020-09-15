from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        self.group_id = 0
        self.M = M
        group = [0] * len(M)
        for i in range(len(M)):
            self.dfs_group(i, group)
        return self.group_id

    def dfs_group(self, i, group):
        if i >= len(self.M):
            return
        if group[i] == 0:
            self.group_id += 1
        group[i] = self.group_id
        for j in range(0, len(self.M)):
            if group[j] != 0:
                continue
            if self.M[i][j] == 1:
                group[j] = self.group_id
                self.dfs_group(j, group)



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