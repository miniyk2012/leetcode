"""replace constructor with factory method
"""
import abc


class Employee(metaclass=abc.ABCMeta):
    ENGINEER = 0
    SALESMAN = 1

    __create_key = object()

    def __init__(self, create_key):
        """How do I create a private constructor?
        https://stackoverflow.com/questions/8212053/private-constructor-in-python"""
        assert (create_key == Employee.__create_key), \
            "OnlyCreatable objects must be created using OnlyCreatable.create"

    @classmethod
    def create(cls, _type):
        if _type == Employee.ENGINEER:
            return Engineer(Employee.__create_key)
        elif _type == Employee.SALESMAN:
            return SalesMan(Employee.__create_key)
        else:
            raise RuntimeError("invalid employee type")

    @classmethod
    def create_by_name(cls, _type_name):
        try:
            import importlib
            return getattr(importlib.import_module(__name__), _type_name)(Employee.__create_key)
        except AttributeError:
            raise TypeError(f"不存在{_type_name}类型的员工")

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


def test_employee():
    engineer = Employee.create(Employee.ENGINEER)
    print(engineer.describe())
    salesman = Employee.create(Employee.SALESMAN)
    print(salesman.describe())
    salesman = Employee.create_by_name('SalesMan')
    print(salesman.describe())

    try:
        SalesMan('1')
    except AssertionError:
        pass
    else:
        raise RuntimeError('不能用构造函数实例化类, 必须用工厂方法实例化类')

    try:
        Employee.create_by_name('Manager')
    except TypeError:
        pass
    else:
        raise RuntimeError('不应该进入这里')


if __name__ == '__main__':
    test_employee()
