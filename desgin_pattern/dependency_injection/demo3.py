from bottle import Bottle


def uses_service(l, m, n):
    def outer(index):
        def wrapper(l=l, m=m, n=n):
            return index(l, m, n)

        return wrapper

    return outer


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


app = Bottle()

a = ServiceA()
b = ServiceB(a)
c = ServiceC(a, b)


@app.get('/')
@uses_service(a, b, c)
def index(x, y, z):
    x.do_work()
    print()
    y.do_work()
    print()
    z.do_work()
    return 'hello world'


def app_test():
    a = ServiceA()
    b = ServiceB(a)
    c = ServiceC(a, b)

    app = Bottle()

    def index(x, y, z):
        x.do_work()
        print()
        y.do_work()
        print()
        z.do_work()
        return 'hello world'

    ret = app.get('/')(uses_service(a, b, c)(index))()
    print(ret)


if __name__ == '__main__':
    app_test()

    # print("run app")
    # run(app)
