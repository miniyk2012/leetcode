# https://leetcode-cn.com/problems/n-queens/
from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        if n == 1:
            return [['Q']]
        result = []
        for j in range(0, n):
            board = self.build_board(n)
            board[0][j] = 'Q'
            self.solve(1, board, result)
        result = self.transform_result(result)
        return result

    def transform_result(self, old_result):
        result = []
        for board in old_result:
            new_board = []
            for line in board:
                new_board.append(''.join(line))
            result.append(new_board)
        return result

    def build_board(self, n):
        """构建全.棋盘"""
        board = []
        for _ in range(n):
            board.append(['.'] * n)
        return board

    def solve(self, i, board, result):
        """已经放好了0~i-1行, 继续往board放第i行, 并找出所有结果"""
        if i == self.n - 1:
            for j in range(0, self.n):
                if not self.conflict(i, j, board):
                    board[i][j] = 'Q'
                    result.append(copy.deepcopy(board))
                    board[i][j] = '.'
            return
        for j in range(0, self.n):
            if not self.conflict(i, j, board):
                board[i][j] = 'Q'
                self.solve(i + 1, board, result)
                board[i][j] = '.'

    def conflict(self, i, j, board):
        """往棋牌放(i,j)时, 是否和前面的行冲突, 有冲突返回True, 否则返回False"""
        # 对角线
        row, column = i - 1, j - 1
        while row >= 0 and column >= 0:
            if board[row][column] == 'Q':
                return True
            row -= 1
            column -= 1

        row, column = i - 1, j + 1
        while row >= 0 and column < self.n:
            if board[row][column] == 'Q':
                return True
            row -= 1
            column += 1

        # 列
        for row in range(0, i):
            if board[row][j] == 'Q':
                return True
        return False

    def print_board(self, board):
        for line in board:
            print(line)


if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(8)
    for board in result:
        solution.print_board(board)
        print()
    print('num =', len(result))
