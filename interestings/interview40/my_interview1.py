from random import randint


class Solution:

    def solve(self, n, m):
        """傻逼方法"""
        ret = [1] * m
        n_cents = int(n * 100 - m)
        for _ in range(n_cents):
            idx = randint(0, m - 1)
            ret[idx] += 1
        ret = list(map(lambda e: e/100, ret))
        return ret

    def solve2(self, n, m):
        """递归写法"""
        n = int(n * 100)
        for ret in self.recursion(n, m, []):
            yield ret

    def recursion(self, n, m, ret):
        if (n == 0 and m > 0) or (n > 0 and m == 0):
            return
        if n == 0 and m == 0:
            yield ret
        for amount in range(1, n + 1):
            ret.append(amount/100)
            yield from self.recursion(n-amount, m-1, ret)
            ret.pop()


if __name__ == '__main__':
    s = Solution()
    ret = s.solve(0.1, 7)
    print(ret)
    print('递归写法')
    i = 0
    for ret in s.solve2(0.1, 7):
        print(ret)
        i += 1
        if i > 4:
            break
