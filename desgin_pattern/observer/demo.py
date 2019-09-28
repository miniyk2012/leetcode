class Man:
    def __init__(self, name):
        self.name = name

    def do_work(self):
        print(f'{self.name} is doing work')


class Clerk:
    actions = []

    @classmethod
    def attach(cls, *action):
        cls.actions.extend(action)

    @classmethod
    def remove(cls, *actions):
        for action in actions:
            cls.actions.remove(action)

    @classmethod
    def notify(cls):
        for action in cls.actions:
            action()


if __name__ == '__main__':
    m1 = Man('yangkai')
    m2 = Man('wuzhenhua')
    Clerk.attach(m1.do_work, m2.do_work)  # 闭包
    Clerk.notify()

    print('-------------------')
    del m1  # 原对象删除后, 闭包仍然存在, 若不释放有内存泄漏风险
    Clerk.notify()

    print('-------------------')
    Clerk.remove(m2.do_work)
    Clerk.notify()



