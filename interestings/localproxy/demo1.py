from werkzeug.local import Local, LocalStack, LocalProxy


class User:
    def __init__(self, name):
        self.name = name
        print('init')

    def __repr__(self):
        return 'name is ' + self.name


def local_demo():
    l = Local()
    request = l('request')
    user = l('user')  # user是代理
    l.user = User('杨恺')
    print(user)
    user.name = 'bb'
    print(user)


def localstack_demo():
    ls = LocalStack()
    a = ls.push(100)
    # a.pop()
    b = ls.push(120)
    print(a, b)
    print(ls.pop())
    print(ls.pop())


def local_proxy():
    xx = LocalProxy(lambda: User('yangkai'))  # 此时原对象的__init__方法尚未被调用
    # xx = User('zz')
    print('call xx')
    print(xx)


if __name__ == '__main__':
    # local_demo()
    # localstack_demo()
    local_proxy()
