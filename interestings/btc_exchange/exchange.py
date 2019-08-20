from pandas import DataFrame

from utils import assert_msg


class ExchangeAPI:
    def __init__(self, data: DataFrame, cash, commission):
        """

        :param data:
        :param cash:
        :param commission: 手续费率
        """
        assert_msg(0 < cash, " 初始现金数量大于 0，输入的现金数量：{}".format(cash))
        assert_msg(0 <= commission <= 0.05, " 合理的手续费率一般不会超过 5%，输入的费率：{}".format(commission))
        self._inital_cash = cash
        self._data = data
        self._commission = commission
        self._position = 0
        self._cash = cash
        self._i = 0

    @property
    def cash(self):
        """
        :return: 返回当前账户现金数量
        """
        return self._cash

    @property
    def position(self):
        """
        :return: 返回当前账户仓位
        """
        return self._position

    @property
    def initial_cash(self):
        """
        :return: 返回初始现金数量
        """
        return self._inital_cash

    @property
    def market_value(self):
        """
        :return: 返回当前市值
        当前市值 = 现金 + 当前仓位 * 比特币当前价格
        """
        return self._cash + self._position * self.current_price

    @property
    def current_price(self):
        """
        :return: 返回当前市场价格
        """
        return self._data.Close[self._i]

    def buy(self):
        """
        用当前账户剩余资金，按照市场价格全部买入
        买到的数量 = 投入的资金 * (1.0 - 手续费) / 价格
        """
        self._position = float(self._cash / (self.current_price * (1 + self._commission)))
        self._cash = 0.0

    def sell(self):
        """
        卖出当前账户剩余持仓
        卖出的收益 = 持有的数量 * 价格 *  (1.0 - 手续费)
        """
        self._cash += float(self._position * self.current_price * (1 - self._commission))
        self._position = 0.0

    def next(self, tick):
        self._i = tick
