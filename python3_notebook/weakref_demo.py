import weakref

class X:
    def __del__(self):
        print(hex(id(self)), 'dead')



if __name__ == '__main__':
    a = X()
    b = a
    a.name = '我是a'
    print(weakref.getweakrefcount(a))
    print(weakref.getweakrefs(a))
    p = weakref.proxy(a)
    w = weakref.ref(a)
    print(weakref.getweakrefcount(a))
    print(weakref.getweakrefs(a))
    print(hex(id(w)))
    print(w().name)
    print(w() is a)
    print()
    print(p.name)
    print(hex(id(p)))
    print(hex(id(w())))
    del a
    print(p.name)
    print(w)
    del b
    print(w)



