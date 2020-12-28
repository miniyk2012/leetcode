class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

    # data descriptor
    def __set__(self, instance, value=0):
        pass


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        pass

    @lazyproperty
    def area(self, value=0):
        print("Com")
        if value == 0 and self.radius == 0:
            raise TypeError("Something went wring")

        return math.pi * value * 2 if value != 0 else math.pi * self.radius * 2

    def test(self):
        pass


if __name__ == '__main__':
    c = Circle(10)
    print(c.area)
    print(c.area)
    print(c.__dict__)
    print(Circle.__dict__)
