class ServiceA(object):
    def do_work(self):
        print("do work")

    @classmethod
    def get_instance(cls):
        return cls()


class ServiceB(object):
    def __init__(self, service):
        self.service = service

    def do_work(self):
        self.service.get_instance().do_work()


class ServiceC(object):
    def do_work(self):
        pass


if __name__ == '__main__':
    """
    If object A depends on object B, object A must not create of import object B directly. 
    Instead of this, object A must provide a way for injecting object B. (eg: construction)
    The responsibility of object creation and dependency injection are delegated to external code.
    
    
    """
    ServiceB(ServiceA).do_work()
