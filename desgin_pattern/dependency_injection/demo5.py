from bottle import Bottle, run


class ServiceA(object):
    def do_work(self):
        print("a do work")


class ServiceB(object):
    def __init__(self, service):
        self.service = service

    def do_work(self):
        self.service.do_work()
        print("b do work")


class ServiceC(object):
    def __init__(self, service_a, service_b):
        self.service_a = service_a
        self.service_b = service_b

    def do_work(self):
        self.service_a.do_work()
        self.service_b.do_work()
        print()


def index(x, y, z):
    x.do_work()
    print()
    y.do_work()
    print()
    z.do_work()
    return 'hello world'


def create_app(a, b, c, index):
    app = Bottle()

    @app.get('/')
    def func():
        return index(a, b, c)

    return app


def app_test():
    a = ServiceA()
    b = ServiceB(a)
    c = ServiceC(a, b)

    ret = index(a, b, c)
    print(ret)


if __name__ == '__main__':
    app_test()

    a = ServiceA()
    b = ServiceB(a)
    c = ServiceC(a, b)

    print("run app")
    app = create_app(a, b, c, index)
    run(app)
