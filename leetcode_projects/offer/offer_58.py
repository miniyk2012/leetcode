class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]

    def reverseLeftWords2(self, s: str, n: int) -> str:
        """不允许用切片"""
        res = []
        for i in range(n, n+len(s)):
            res.append(s[i%len(s)])
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseLeftWords2('lrloseumgh', 6))
