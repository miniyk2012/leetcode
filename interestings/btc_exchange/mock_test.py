from backtest import Backtest
from exchange import ExchangeAPI
from strategies.sma_cross import SmaCross
from utils import read_file


def main():
    BTCUSD = read_file('BTCUSD_GEMINI.csv')
    ret = Backtest(BTCUSD, SmaCross, ExchangeAPI, 10000.0, 0.00).run()
    print(ret)


if __name__ == '__main__':
    main()
