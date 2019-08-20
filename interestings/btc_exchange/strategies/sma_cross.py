from utils import crossover, SMA
from strategy import Strategy


class SmaCross(Strategy):
    # 小窗口 SMA 的窗口大小，用于计算 SMA 快线
    fast = 10

    # 大窗口 SMA 的窗口大小，用于计算 SMA 慢线
    slow = 20

    def init(self):
        # 计算历史上每个时刻的快线和慢线
        self.sma1 = self.I(SMA, self.data.Close, self.fast)
        self.sma2 = self.I(SMA, self.data.Close, self.slow)

    def next(self, tick):
        # 如果此时快线刚好越过慢线，买入全部
        if crossover(self.sma1[:tick], self.sma2[:tick]):
            self.buy()

        # 如果是慢线刚好越过快线，卖出全部
        elif crossover(self.sma2[:tick], self.sma1[:tick]):
            self.sell()

        # 否则，这个时刻不执行任何操作。
        else:
            pass
