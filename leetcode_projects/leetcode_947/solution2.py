from typing import List

class UnionSet:
    def __init__(self):
        self.parent = dict()
        self.count = 0

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.count -= 1
        self.parent[root_x] = self.parent[root_y]


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        我们将这个二维平面抽象为图，把石子看作「点」，石子间的同行或同列关系看作「边」。如果两个石子同属某一行或某一列，我们就认为这两个石子之间有一条边
        一定可以把一个连通图里的所有顶点根据这个规则删到只剩下一个顶点
        最多可以移除的石头的个数 = 所有石头的个数 - 连通分量的个数
        若无须给出移除石头的顺序, 可以用并查集的方法直接求出联通分量个数, 这最简单
        并查集里的元素是 描述「横坐标」和「纵坐标」的数值, 「合并」的语义是：所有横坐标为 x 的石头和所有纵坐标为 y 的石头都属于同一个连通分量。

        若要给出移除石头顺序的方案, 可以通过遍历的方式（深度优先遍历或者广度优先遍历）遍历到这个连通图的所有顶点, 那么就可以按照遍历的方式 逆向 移除石头，最后只剩下一块石头。
        """
        union_set = UnionSet()
        for x, y in stones:
            # 递归法理解该问题, 假设所有联通的节点都在同一个集合里, 新加入的节点, 若(x, y+10001)都不在某个集合里, 则它自身新建了个集合;
            # 否则(x, y+10001)有个坐标肯定在已知3的一个集合里, 那把另一个坐标加入就行了. 这个语义是正确的, 但理解起来还是有点难度的.
            union_set.union(x, y + 10001)
        return len(stones) - union_set.count


if __name__ == '__main__':
    s = Solution()
    stones = [[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]
    assert s.removeStones(stones) == 5
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    assert s.removeStones(stones) == 5
    stones = [[0, 0]]
    assert s.removeStones(stones) == 0
