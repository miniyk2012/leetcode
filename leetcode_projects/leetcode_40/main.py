from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.rets = []
        self.dfs(0, target, [])
        return self.rets

    def dfs(self, x, target, ret):
        if target == 0:
            self.rets.append(ret[:])
            return
        dic = set()
        for i in range(x, len(self.candidates)):
            if target < self.candidates[i]:
                break
            if self.candidates[i] in dic:
                continue
            ret.append(self.candidates[i])
            dic.add(self.candidates[i])
            self.dfs(i + 1, target - self.candidates[i], ret)
            ret.pop(-1)


if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    s = Solution()
    print(s.combinationSum2(candidates, target))
