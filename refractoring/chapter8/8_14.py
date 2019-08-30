"""replace typecode with subclasses
以子类取代类型码"""

import abc


class Employee(metaclass=abc.ABCMeta):
    ENGINEER = 0
    SALESMAN = 1
    MANAGER = 2

    @property
    @abc.abstractmethod
    def occupation_type(self):
        pass

    @classmethod
    def create(cls, _type):
        if _type == Employee.ENGINEER:
            return Engineer()
        elif _type == Employee.SALESMAN:
            return SalesMan()
        elif _type == Employee.MANAGER:
            return Manager()

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


if __name__ == "__main__":
    test_employee()
