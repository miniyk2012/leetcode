"""以明确函数取代参数
"""
import abc


class Employee(metaclass=abc.ABCMeta):
    __create_key = object()

    def __init__(self, create_key):
        """How do I create a private constructor?
        https://stackoverflow.com/questions/8212053/private-constructor-in-python"""
        assert (create_key == Employee.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"

    @classmethod
    def create_engineer(cls):
        return Engineer(Employee.__create_key)

    @classmethod
    def create_salesman(cls):
        return SalesMan(Employee.__create_key)

    @abc.abstractmethod
    def describe(self):
        pass


class Engineer(Employee):
    def describe(self):
        return 'ENGINEER'


class SalesMan(Employee):
    def describe(self):
        return 'SALESMAN'


def test_employee():
    engineer = Employee.create_engineer()
    print(engineer.describe())
    salesman = Employee.create_salesman()
    print(salesman.describe())

    try:
        SalesMan('1')
    except AssertionError:
        pass
    else:
        raise RuntimeError('不能用构造函数实例化类, 必须用工厂方法实例化类')


if __name__ == '__main__':
    test_employee()
