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
        self.price_code = price_code

    def get_price_code(self):
        return self.price_code

    def set_price_code(self, arg):
        self.price_code = arg

    def get_title(self):
        return self.title
