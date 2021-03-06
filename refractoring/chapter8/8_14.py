"""replace typecode with subclasses
以子类取代类型码"""

import abc


class Employee(metaclass=abc.ABCMeta):
    ENGINEER = 0
    SALESMAN = 1
    MANAGER = 2

    __create_key = object()

    def __init__(self, create_key):
        """How do I create a private constructor?
        https://stackoverflow.com/questions/8212053/private-constructor-in-python"""
        assert (create_key == Employee.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"

    @property
    @abc.abstractmethod
    def occupation_type(self):
        pass

    @classmethod
    def create(cls, _type):
        if _type == Employee.ENGINEER:
            return Engineer(Employee.__create_key)
        elif _type == Employee.SALESMAN:
            return SalesMan(Employee.__create_key)
        elif _type == Employee.MANAGER:
            return Manager(Employee.__create_key)

    @abc.abstractmethod
    def describe(self):
        pass


class Engineer(Employee):
    def describe(self):
        return 'ENGINEER'

    @property
    def occupation_type(self):
        return Employee.ENGINEER


class SalesMan(Employee):
    def describe(self):
        return 'SALESMAN'

    @property
    def occupation_type(self):
        return Employee.SALESMAN


class Manager(Employee):
    def describe(self):
        return 'MANAGER'

    @property
    def occupation_type(self):
        return Employee.MANAGER


def test_employee():
    engineer = Employee.create(Employee.ENGINEER)
    print(engineer.describe())
    print(engineer.occupation_type)
    salesman = Employee.create(Employee.SALESMAN)
    print(salesman.describe())
    print(salesman.occupation_type)
    manager = Employee.create(Employee.MANAGER)
    print(manager.describe())
    print(manager.occupation_type)
    try:
        Manager('1')
    except AssertionError:
        pass
    else:
        raise RuntimeError('不能用构造函数实例化类, 必须用工厂方法实例化类')


if __name__ == "__main__":
    test_employee()
