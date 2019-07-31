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
