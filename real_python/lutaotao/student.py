class Score:
    def __init__(self, default=0):
        self._score = default

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Score must be integer')
        if not 0 <= value <= 100:
            raise ValueError('Valid value must be in [0, 100]')

        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __del__(self):
        del self._score


class Student:
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "<Student: {}, math:{}, chinese: {}, english:{}>".format(
            self.name, self.math, self.chinese, self.english
        )


if __name__ == '__main__':
    std1 = Student('小明', 12, 3, 45)
    print(std1.math)
    std2 = Student('小王', 72, 3, 45)
    print(std2.math)
    print(std1.math)

