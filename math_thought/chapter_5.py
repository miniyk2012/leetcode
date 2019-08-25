"""题目：
有四种面额的货币, 1, 2, 5, 10元。一共奖赏10元, 如果考虑每次的金额和先后顺序, 一共有多少种不同的奖赏方式呢？"""


class Solution:
    MONEY = [1, 2, 5, 10]
    def permutate(self, total):
        self.total = total
        self._ret = []
        self.dfs(0, [])
        return self._ret
        
    def dfs(self, current_money, current_selections):
        if current_money == self.total:
            self._ret.append(current_selections[:])
            return
        for money in Solution.MONEY:
            if money + current_money > self.total:
                break
            current_selections.append(money)
            self.dfs(current_money + money, current_selections)
            current_selections.pop()

if __name__ == "__main__":
    s = Solution()
    print(s.permutate(10))
        