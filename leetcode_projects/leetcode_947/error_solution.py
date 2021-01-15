from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """通过构造法找出可以移除的最大石头
        位于水平和竖直方向交叉点的石头不能过早移除
        我写的这个方法可以作为一个错误例子, 作为参考"""
        row_index, col_index = self.build_row_col_index(stones)
        total = 0
        # 下面这种方案无脑删节点, 过早移除了位于水平和竖直方向交叉点的石头, 因此产生了错误
        for stone in stones[:]:
            x, y = stone[0], stone[1]
            if (y in row_index and len(row_index[y]) > 1) or (x in col_index and len(col_index[x]) > 1):
                total += 1
                row_index[y].remove(x)
                col_index[x].remove(y)
        return total

    def build_row_col_index(self, stones):
        row_index = dict()
        col_index = dict()
        for stone in stones:
            x, y = stone[0], stone[1]
            if x not in col_index:
                col_index[x] = set([y])
            else:
                col_index[x].add(y)
            if y not in row_index:
                row_index[y] = set([x])
            else:
                row_index[y].add(x)
        for k in row_index.keys():
            row_index[k] = sorted(list(row_index[k]))
        for k in col_index.keys():
            col_index[k] = sorted(list(col_index[k]))
        return row_index, col_index


if __name__ == '__main__':
    s = Solution()
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    assert s.removeStones(stones) == 5
    stones = [[0, 0]]
    assert s.removeStones(stones) == 0
    # 下面这个用例通不过
    stones = [[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]]
    assert s.removeStones(stones) == 5
