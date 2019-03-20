from abc import ABCMeta, abstractmethod
from decimal import Decimal


class AbstractFactory(metaclass=ABCMeta):

    @abstractmethod
    def build_sequence(self):
        pass

    @abstractmethod
    def build_number(self, string):
        pass

    @abstractmethod
    def add_item(self, container, item):
        pass


class Loader(object):
    @staticmethod
    def load(s, factory):
        sequence = factory.build_sequence()
        for substring in s.split(','):
            item = factory.build_number(substring)
            factory.add_item(sequence, item)
        return sequence


class DecimalFactory(AbstractFactory):
    def build_sequence(self):
        return []

    def build_number(self, s):
        return Decimal(s)

    def add_item(self, container, item):
        container.append(item)


class FloatFactory(AbstractFactory):
    def build_sequence(self):
        return set()

    def build_number(self, s):
        return float(s)

    def add_item(self, container, item):
        container.add(item)


def main():
    f = DecimalFactory()
    result = Loader.load('1.23, 4.56, 4.56', f)
    print(result)

    f = FloatFactory()
    result = Loader.load('1.23, 4.56, 4.56', f)
    print(result)


if __name__ == '__main__':
    main()
