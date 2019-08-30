"""9.6: replace conditional with polymorphism
8.15: replace type code with state/strategy
"""

import abc


class Employee:
    def __init__(self, _type):
        self.occupation_type = _type
        self._monthly_salary = 100
        self._commission = 20
        self._bonus = 50

    def pay_amount(self):
        return self._type.pay_amount(self)

    @property
    def occupation_type(self):
        return self._type.type_code()

    @occupation_type.setter
    def occupation_type(self, _type):
        self._type: EmployeeType = EmployeeType.new_type(_type)


class EmployeeType(metaclass=abc.ABCMeta):
    ENGINEER = 0
    SALESMAN = 1
    MANAGER = 2

    @abc.abstractmethod
    def pay_amount(self, employee: Employee):
        pass

    @abc.abstractmethod
    def type_code(self):
        pass

    @classmethod
    def new_type(cls, _type):
        if _type == EmployeeType.ENGINEER:
            return Engineer()
        elif _type == EmployeeType.SALESMAN:
            return SalesMan()
        elif _type == EmployeeType.MANAGER:
            return Manager()
        else:
            raise RuntimeError('Incorrect Employee')


class Engineer(EmployeeType):
    def pay_amount(self, employee: Employee):
        return employee._monthly_salary

    def type_code(self):
        return self.ENGINEER


class SalesMan(EmployeeType):
    def pay_amount(self, employee: Employee):
        return employee._monthly_salary + employee._commission

    def type_code(self):
        return self.SALESMAN


class Manager(EmployeeType):
    def pay_amount(self, employee: Employee):
        return employee._monthly_salary + employee._bonus

    def type_code(self):
        return self.MANAGER


def test_employee():
    e = Employee(EmployeeType.ENGINEER)
    print(e.occupation_type)
    print(e.pay_amount())
    e.occupation_type = EmployeeType.MANAGER
    print(e.occupation_type)
    print(e.pay_amount())
    e.occupation_type = EmployeeType.SALESMAN
    print(e.occupation_type)
    print(e.pay_amount())


if __name__ == '__main__':
    test_employee()
