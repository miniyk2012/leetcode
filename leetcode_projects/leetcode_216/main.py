from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.rets = []
        self.dfs(1, k, n, [])
        return self.rets

    def dfs(self, x, k, n, result):
        if k == 0 and n == 0:
            self.rets.append(result[:])
            return
        for i in range(x, 10):
            if i > n:
                break
            result.append(i)
            self.dfs(i + 1, k - 1, n - i, result)
            result.pop(-1)


if __name__ == '__main__':
    s = Solution()
    rets = s.combinationSum3(3, 7)
    print(rets)

    rets = s.combinationSum3(3, 9)
    print(rets)
