from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        a = self.flip(A)
        a = self.invert(a)
        return a

    def flip(self, a):
        mat = []
        for row in a:
            mat.append(row[::-1])
        return mat

    def invert(self, a):
        mat = []
        for row in a:
            mat.append(self.invert_row(row))
        return mat

    def invert_row(self, row):
        return [0 if e == 1 else 1 for e in row]
