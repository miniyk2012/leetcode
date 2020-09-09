from typing import List


class Solution:
    def permutation2(self, s: str) -> List[str]:
        """全排列"""
        self.rets = []
        self.s_list = list(s)
        self.dfs2(self.s_list, "")
        return self.rets

    def dfs2(self, remain, ret):
        if not remain:
            self.rets.append(ret)
            return
        dic = set()
        for i in range(len(remain)):
            c = remain[i]
            if c in dic:  # 剪枝
                continue
            dic.add(c)
            remain.pop(i)
            self.dfs2(remain, ret + c)
            remain.insert(i, c)

    def permutation(self, s: str) -> List[str]:
        """全排列"""
        self.rets = []
        self.s = s
        self.dfs(0, list(s))
        return self.rets

    def dfs(self, x, c):
        if x == len(self.s) - 1:
            self.rets.append(''.join(c))
            return
        dic = set()
        for i in range(x, len(self.s)):
            if c[i] in dic:
                continue
            dic.add(c[i])
            c[x], c[i] = c[i], c[x]
            self.dfs(x + 1, c)
            c[i], c[x] = c[x], c[i]


if __name__ == '__main__':
    s = Solution()
    print(s.permutation2("abc"))
    print(s.permutation2("aba"))
    print(s.permutation2("ryawrowv"))
