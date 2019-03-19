from __future__ import annotations


class Employee:
    def __init__(self, name):
        self.name = name
        try:
            self._manager = NO_MANAGER
        except NameError:
            self._manager = self

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        self._manager = value

    def display_name(self):
        return self.name


NO_MANAGER = Employee(name='no acting manager')

if __name__ == '__main__':
    employees = [Employee(str(i)) for i in range(5)]

    manager = Employee('manager')

    for e in employees:
        e.manager = manager

    employees.append(Employee('5'))
    employees.insert(3, NO_MANAGER)

    # 使用方法1
    for e in employees:
        m = e.manager.display_name()
        print(e.name, '-', m)
    print('*' * 10)
    # 使用方法2
    for e in employees:
        if e.manager is not NO_MANAGER:
            m = e.manager.display_name()
            print(e.name, '-', m)
