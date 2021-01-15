from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        我们将这个二维平面抽象为图，把石子看作「点」，石子间的同行或同列关系看作「边」。如果两个石子同属某一行或某一列，我们就认为这两个石子之间有一条边
        一定可以把一个连通图里的所有顶点根据这个规则删到只剩下一个顶点
        最多可以移除的石头的个数 = 所有石头的个数 - 连通分量的个数
        若无须给出移除石头的顺序, 可以用并查集的方法直接求出联通分量个数, 这最简单
        若要给出移除石头顺序的方案, 可以通过遍历的方式（深度优先遍历或者广度优先遍历）遍历到这个连通图的所有顶点, 那么就可以按照遍历的方式 逆向 移除石头，最后只剩下一块石头。
        """
        pass


if __name__ == '__main__':
    s = Solution()
    stones = [[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]
    assert s.removeStones(stones) == 5
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    assert s.removeStones(stones) == 5
    stones = [[0, 0]]
    assert s.removeStones(stones) == 0
