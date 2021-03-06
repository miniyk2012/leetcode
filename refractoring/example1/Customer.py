from typing import List

from rental import Rental
from statement import TextStatment


class Customer:
    """ 顾客类，存放每个顾客租赁信息的列表

    :param name: 顾客姓名
    """

    def __init__(self, name):
        self.name = name
        self.rentals: List[Rental] = []

    def add_rental(self, rental: Rental):
        """ 增加一条租赁信息

        :param rental: object, Rental类
        """
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def html_statement(self):
        pass

    def text_statement(self):
        """生成详单的函数"""
        return TextStatment.value(self)

    def get_total_charge(self):
        result = 0
        for retal in self.rentals:
            result += retal.get_charge()
        return result

    def get_total_frequent_point(self):
        result = 0
        for retal in self.rentals:
            result += retal.get_frequent_point()
        return result
