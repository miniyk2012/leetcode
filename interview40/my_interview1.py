from random import randint


class Solution:

    def solve(self, n, m):
        ret = [1] * m
        n_cents = n * 100 - m
        for _ in range(n_cents):
            idx = randint(0, m - 1)
            ret[idx] += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    ret = s.solve(5, 10)
    print(ret)
    assert sum(ret) == 5 * 100
