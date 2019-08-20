from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self._candidates = candidates
        self._len = len(candidates)
        self.ret = []
        self.recursion(0, target, [])
        return self.ret

    def recursion(self, start, left, current_list):
        if start >= self._len:
            return
        self.recursion(start + 1, left, current_list[:])  # 该位置不取
        current_val = self._candidates[start]
        left = left - current_val
        while left > 0:
            current_list.append(current_val)
            self.recursion(start + 1, left, current_list[:])  # 该位置分别取1~多次, 再进入下个位置, 即DFS
            left = left - current_val
        if left == 0:
            current_list.append(current_val)
            self.ret.append(current_list)


def test():
    def assert_equal_list(l1: List[List[int]], l2: List[List[int]]):
        print(f'l1={l1}\nl2={l2}')
        assert len(l1) == len(l2)
        assert set(tuple(e) for e in l1) == set(tuple(e) for e in l2)
        print()

    s = Solution()

    candidates = [2, 3, 6, 7]
    target = 7
    expected = [
        [7],
        [2, 2, 3]
    ]
    assert_equal_list(s.combinationSum(candidates, target), expected)

    candidates = [2, 3, 5]
    target = 8
    expected = [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
    assert_equal_list(s.combinationSum(candidates, target), expected)


if __name__ == '__main__':
    test()
