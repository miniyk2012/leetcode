class ServiceA(object):
    def do_work(self):
        print("do work")

    @classmethod
    def get_instance(cls):
        return cls()


class ServiceB(object):
    def do_work(self):
        ServiceA.get_instance().do_work()


class ServiceC(object):
    def do_work(self):
        pass


if __name__ == '__main__':
    ServiceB().do_work()
