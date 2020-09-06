class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = list(range(1, n + 1))
        ret = ''
        mod, i = k, 1
        while mod > 0:
            div, mod = divmod(mod, self.factorial(n - i))
            if mod == 0:
                digit = digits.pop(div - 1)
            else:
                digit = digits.pop(div)
            ret += str(digit)
            i += 1
        digits = digits[::-1]
        for _, digit in enumerate(digits):
            ret += str(digit)
        return ret

    def factorial(self, m):
        ret = 1
        for i in range(1, m + 1):
            ret *= i
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(4, 9))
    print(solution.getPermutation(3, 3))
    print(solution.getPermutation(1, 1))
    print(solution.getPermutation(3, 2))
