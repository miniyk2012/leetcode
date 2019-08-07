from typing import List

from leetcode_projects.data_structs import UnionFindSet


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        ufs = UnionFindSet(len(M))
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1:
                    ufs.union(i, j)

        circles = set()
        for i in range(len(M)):
            circles.add(ufs.find(i))

        return len(circles)


def test1():
    s = Solution()
    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    assert s.findCircleNum(M) == 2


def test2():
    s = Solution()
    M = [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]]
    assert s.findCircleNum(M) == 1


if __name__ == '__main__':
    test1()
    test2()