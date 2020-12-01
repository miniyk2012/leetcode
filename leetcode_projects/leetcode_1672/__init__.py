from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = [0] * len(accounts)
        for i in range(len(wealth)):
            wealth[i] = sum(accounts[i])
        return max(wealth)

if __name__ == '__main__':
    accounts = [[1,2,3],[3,2,1]]
    s = Solution()
    assert s.maximumWealth(accounts) == 6