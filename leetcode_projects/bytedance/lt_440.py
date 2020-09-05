class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """字符串排序"""
        num = 0
        digit_length = len(str(n))
        first_digit = int(str(n)[0])
        pass

    def findKthNumberSlow(self, n: int, k: int) -> int:
        """慢速法"""
        a = [str(i) for i in range(1, n + 1)]
        a.sort()
        return a[k - 1]


if __name__ == '__main__':
    solution = Solution()
    ret1 = solution.findKthNumber(130, 5)
    ret2 = solution.findKthNumberSlow(5430, 19)
    print(ret1, ret2)
