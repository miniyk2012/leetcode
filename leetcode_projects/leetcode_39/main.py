from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = sorted(candidates)  # 排个序, 方便后续剪枝
        self.rets = []
        self.dfs(0, target, [])
        return self.rets

    def dfs(self, start, target, ret):
        if target == 0:
            self.rets.append(ret[:])  # 比如ret==[2,3,3]
            return
        for i in range(start, len(self.candidates)):
            candidate = self.candidates[i]
            if target < candidate:
                break  # 排序后, 可以直接break, 剪枝繁更快
            ret.append(candidate)
            self.dfs(i, target - candidate, ret)
            ret.pop(-1)


def test():
    def assert_equal_list(l1: List[List[int]], l2: List[List[int]]):
        print(f'result={l1}\nexpect={l2}')
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
