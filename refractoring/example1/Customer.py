from movie import Movie


class Customer:
    """ 顾客类，存放每个顾客租赁信息的列表

    :param name: 顾客姓名
    """

    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        """ 增加一条租赁信息

        :param rental: object, Rental类
        """
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        """ 生成详单的函数 """
        total_amount = 0.0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"
        for retal in self.rentals:
            this_amount = 0

            # 计算每部影片的价格
            if retal.get_movie().get_price_code() == Movie.REGULAR:
                this_amount += 2
                if retal.get_days_rented() > 2:
                    this_amount += (retal.get_days_rented() - 2) * 1.5
            elif retal.get_movie().get_price_code() == Movie.NEW_REALEASE:
                this_amount += retal.get_days_rented() * 3
            elif retal.get_movie().get_price_code() == Movie.CHILDRENS:
                this_amount += 1.5
                if retal.get_days_rented() > 3:
                    this_amount += (retal.get_days_rented() - 3) * 1.5

            # 计算常客积分
            frequent_renter_points += 1
            # 新片租赁两天以上会有额外的积分奖励
            if retal.get_movie().get_price_code() == Movie.NEW_REALEASE and \
                    retal.get_days_rented() > 1:
                frequent_renter_points += 1

            # 展示一条影片租赁的详情
            result += "\t" + retal.get_movie().get_title() + "\t" \
                      + str(this_amount) + "\n"

            total_amount += this_amount

        # 汇总信息
        result += "Amount owned is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) \
                  + " frequent renter points"
        return result
