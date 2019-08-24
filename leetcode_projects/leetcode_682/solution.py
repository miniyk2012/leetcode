import sys
from typing import List


class Solution:
    """solution"""
    def calPoints(self, ops: List[str]) -> int:
        pointsCal = PointsCal(ops)
        return pointsCal.cal_points()


class PointsCal:
    def __init__(self, ops):
        self.ops = ops
        self.points = []

    def _num_cal(self, idx):
        self.points.append(int(self.ops[idx]))

    def _plus_cal(self):
        point = self.points[-1] + self.points[-2]
        self.points.append(point)

    def _d_cal(self):
        self.points.append(2 * self.points[-1])

    def _c_cal(self):
        self.points.pop()

    def cal_points(self):
        def is_num(token):
            return token.isdigit() or (token.startswith('-') and token[1:].isdigit())
        for idx, token in enumerate(self.ops):
            if is_num(token):
                self._num_cal(idx)
            elif token == '+':
                self._plus_cal()
            elif token == 'D':
                self._d_cal()
            elif token == 'C':
                self._c_cal()
            else:
                raise RuntimeError("point类型错误")
        return sum(self.points)


def test():
    """test"""
    s = Solution()
    ops = ["5", "2", "C", "D", "+"]
    assert s.calPoints(ops) == 30
    ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    assert s.calPoints(ops) == 27


if __name__ == "__main__":
    test()
