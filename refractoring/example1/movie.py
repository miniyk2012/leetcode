import abc
from numbers import Number


class PriceState(metaclass=abc.ABCMeta):
    pass

    @abc.abstractmethod
    def get_charge(self, rented_days: Number):
        pass


class RegularPriceState(PriceState):

    def get_charge(self, rented_days):
        result = 2
        if rented_days > 2:
            result += (rented_days - 2) * 1.5
        return result


class ChildrensPriceState(PriceState):

    def get_charge(self, rented_days):
        result = 1.5
        if rented_days > 3:
            result += (rented_days - 3) * 1.5

        return result


class FrequentPointState:
    def get_frequent_point(self, rented_days):
        return 1


class NewReleaseFrequentPointState(FrequentPointState):
    def get_frequent_point(self, rented_days):
        # 新片租赁两天以上会有额外的积分奖励
        if rented_days > 1:
            return 2
        return 1


class NewReleasePriceState(PriceState):

    def get_charge(self, rented_days: Number):
        return rented_days * 3


class Movie:
    """ 影片类，一个单纯的数据类

        :param title: string, 影片标题
        :param price_code: int, 影片的计价类型
        """

    CHILDRENS = 2  # 儿童片
    REGULAR = 0  # 普通片
    NEW_REALEASE = 1  # 新片

    def __init__(self, title, price_code):
        self.title = title
        self.set_price_code(price_code)

    def get_price_code(self):
        return self.price_code

    def set_price_code(self, arg):
        self.price_code = arg
        self.point_state = FrequentPointState()
        if arg == Movie.REGULAR:
            self.price_state = RegularPriceState()
        elif arg == Movie.CHILDRENS:
            self.price_state = ChildrensPriceState()
        elif arg == Movie.NEW_REALEASE:
            self.price_state = NewReleasePriceState()
            self.point_state = NewReleaseFrequentPointState()

    def get_title(self):
        return self.title

    def get_charge(self, rented_days):
        return self.price_state.get_charge(rented_days)

    def get_frequent_point(self, rented_days):
        return self.point_state.get_frequent_point(rented_days)
