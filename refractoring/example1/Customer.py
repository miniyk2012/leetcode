from typing import List

from rental import Rental


class Customer:
    """ 顾客类，存放每个顾客租赁信息的列表

    :param name: 顾客姓名
    """

    def __init__(self, name):
        self.name = name
        self.rentals: List[Rental] = []

    def add_rental(self, rental):
        """ 增加一条租赁信息

        :param rental: object, Rental类
        """
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def html_statement(self):
        pass

    def statement(self):
        """ 生成详单的函数 """
        result = "Rental Record for " + self.get_name() + "\n"

        for retal in self.rentals:
            # 展示一条影片租赁的详情
            result += "\t" + retal.get_movie().get_title() + "\t" \
                      + str(retal.get_charge()) + "\n"
        # 汇总信息
        result += "Amount owned is " + str(self.get_total_charge()) + "\n"
        result += "You earned " + str(self.get_total_frequent_point()) \
                  + " frequent renter points"
        return result

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
