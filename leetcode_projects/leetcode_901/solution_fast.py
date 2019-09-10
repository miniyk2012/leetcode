class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # 参考了: https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-901-online-stock-span/
        ret = 1
        while self.stack:
            if self.stack[-1][0] <= price:
                ret += self.stack.pop()[1]
            else:
                break
        self.stack.append((price, ret))
        return ret


def test():
    s = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    rets = [1, 1, 1, 2, 1, 4, 6]
    for price, ret in zip(prices, rets):
        assert s.next(price) == ret
