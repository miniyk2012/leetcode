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
        return self.movie.get_charge(self.days_rented)

    def get_frequent_point(self):
        return self.movie.get_frequent_point(self.days_rented)
