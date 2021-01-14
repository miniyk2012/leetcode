from typing import List


class Solution:
    def permutation2(self, s: str) -> List[str]:
        """全排列"""
        self.rets = []
        self.s_list = list(s)
        self.dfs2(self.s_list, "")
        return self.rets

    def dfs2(self, remain, ret):
        if len(remain) == 0:
            self.rets.append(ret)
            return
        swapped = set()
        for i in range(len(remain)):
            c = remain[i]
            if c in swapped:
                continue
            remain.pop(i)
            self.dfs2(remain, ret+c)
            remain.insert(i, c)
            swapped.add(remain[i])


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

    def pailie(self, the_str):
        if type(the_str) != str:
            raise RuntimeError('not type')
        if the_str == '':
            return []
        self.result = []
        for i in range(len(the_str)):
            char = the_str[i]
            remain_str = the_str[:i] + the_str[i + 1:]
            self.pailie_remain(char, remain_str)

        return list(set(self.result))

    def pailie_remain(self, current_str, remain):
        if remain == '':
            self.result.append(current_str)
            return
        for i in range(len(remain)):
            char = remain[i]
            remain_str = remain[:i] + remain[i + 1:]
            new_current = current_str + char
            self.pailie_remain(new_current, remain_str)


if __name__ == '__main__':
    s = Solution()
    print(s.permutation2("abc"))
    print(s.permutation2("aba"))
    print(s.permutation("rya"))

    print(s.pailie('abc'))
