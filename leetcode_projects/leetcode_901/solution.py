class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # 该解法超时
        ret = 1
        temp_stack = []
        while self.stack:
            if self.stack[-1] <= price:
                temp_stack.append(self.stack.pop())
                ret += 1
            else:
                break
        while temp_stack:
            self.stack.append(temp_stack.pop())
        self.stack.append(price)
        return ret


def test():
    s = StockSpanner()
    prices = [100, 80, 60, 70, 60, 75, 85]
    rets = [1, 1, 1, 2, 1, 4, 6]
    for price, ret in zip(prices, rets):
        assert s.next(price) == ret




