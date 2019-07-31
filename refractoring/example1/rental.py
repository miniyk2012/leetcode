from movie import Movie


class Rental:
    """ 租赁类，表示某个顾客租了一部影片

    :param movie: object, Movie类
    :days_rented: int, 租期
    """

    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie

    def get_charge(self):
        result = 0
        # 计算每部影片的价格
        if self.get_movie().get_price_code() == Movie.REGULAR:
            result += 2
            if self.get_days_rented() > 2:
                result += (self.get_days_rented() - 2) * 1.5
        elif self.get_movie().get_price_code() == Movie.NEW_REALEASE:
            result += self.get_days_rented() * 3
        elif self.get_movie().get_price_code() == Movie.CHILDRENS:
            result += 1.5
            if self.get_days_rented() > 3:
                result += (self.get_days_rented() - 3) * 1.5
        return result

    def get_frequent_point(self):
        # 新片租赁两天以上会有额外的积分奖励
        result = 1
        if self.get_movie().get_price_code() == Movie.NEW_REALEASE and \
                self.get_days_rented() > 1:
            result = 2
        return result
