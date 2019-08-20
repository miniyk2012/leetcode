import abc
from numbers import Number


class Price(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def price_code(self):
        pass

    @abc.abstractmethod
    def get_charge(self, rented_days: Number):
        pass

    def get_frequent_point(self, rented_days):
        return 1


class RegularPrice(Price):

    @property
    def price_code(self):
        return Movie.REGULAR

    def get_charge(self, rented_days):
        result = 2
        if rented_days > 2:
            result += (rented_days - 2) * 1.5
        return result


class ChildrensPrice(Price):

    @property
    def price_code(self):
        return Movie.CHILDRENS

    def get_charge(self, rented_days):
        result = 1.5
        if rented_days > 3:
            result += (rented_days - 3) * 1.5

        return result


class NewReleasePrice(Price):

    @property
    def price_code(self):
        return Movie.NEW_REALEASE

    def get_charge(self, rented_days: Number):
        return rented_days * 3

    def get_frequent_point(self, rented_days):
        # 新片租赁两天以上会有额外的积分奖励
        if rented_days > 1:
            return 2
        return 1


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
        return self.price.price_code

    def set_price_code(self, arg):
        if arg == Movie.REGULAR:
            self.price = RegularPrice()
        elif arg == Movie.CHILDRENS:
            self.price = ChildrensPrice()
        elif arg == Movie.NEW_REALEASE:
            self.price = NewReleasePrice()

    def get_title(self):
        return self.title

    def get_charge(self, rented_days):
        return self.price.get_charge(rented_days)

    def get_frequent_point(self, rented_days):
        return self.price.get_frequent_point(rented_days)
