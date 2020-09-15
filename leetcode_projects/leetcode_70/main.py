class Solution:
    def numWays(self, n: int) -> int:
        """"动态规划"""
        if n < 2:
            return 1
        results = [0] * (n + 1)
        results[0] = results[1] = 1
        for i in range(2, n + 1):
            results[i] = (results[i - 1] + results[i - 2]) % 1000000007
        print(results)
        return results[n]


if __name__ == '__main__':
    s = Solution()
    print(s.numWays(7))
