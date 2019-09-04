from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next_borad = []
        for i in range(len(board)):
            next_borad.append([0] * len(board[0]))

        for i in range(len(board)):
            for j in range(len(board[0])):
                next_borad[i][j] = self.apply_rules(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = next_borad[i][j]

    def apply_rules(self, board, y, x):
        lives = 0
        for i in range(max(0, y - 1), min(y + 2, len(board))):
            for j in range(max(0, x - 1), min(x + 2, len(board[0]))):
                if not (i == y and j == x):
                    lives += board[i][j]
        if board[y][x] == 1:
            if lives < 2:
                return 0
            if lives in (2, 3):
                return 1
            else:
                return 0
        else:
            if lives == 3:
                return 1
            return 0


def test():
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s = Solution()
    s.gameOfLife(board)
    assert board == [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1],
        [0, 1, 0]
    ]


if __name__ == '__main__':
    test()
