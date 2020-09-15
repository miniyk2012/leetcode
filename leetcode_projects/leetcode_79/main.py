from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.dfs_visit(board, i, j, visited, word):
                    return True
        return False

    def dfs_visit(self, board, i, j, visited, word):
        if word == '' or board[i][j] == word:
            return True
        if board[i][j] != word[0]:
            return False
        visited[i][j] = True
        if i - 1 >= 0 and not visited[i - 1][j]:
            if self.dfs_visit(board, i - 1, j, visited, word[1:]):
                return True
        if i + 1 < len(board) and not visited[i + 1][j]:
            if self.dfs_visit(board, i + 1, j, visited, word[1:]):
                return True
        if j - 1 >= 0 and not visited[i][j - 1]:
            if self.dfs_visit(board, i, j - 1, visited, word[1:]):
                return True
        if j + 1 < len(board[0]) and not visited[i][j + 1]:
            if self.dfs_visit(board, i, j + 1, visited, word[1:]):
                return True
        visited[i][j] = False
        return False


if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    print(s.exist(board, word))
    word = "SEE"
    print(s.exist(board, word))
    word = "ABCB"
    print(s.exist(board, word))
    print(s.exist([["a"]], "a"))
