from dd import func_d
from __init__ import funcs



def register(func):
    funcs.append(func)
    return func

@register
def func_c1():
    func_d()
    print('c1')

@register
def func_c2():
    print('c2')


print('c code')

if __name__ == '__main__':
    func_c1()
    print(funcs)
