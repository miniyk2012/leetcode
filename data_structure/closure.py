def adder(x):
    def add(y):
        nonlocal x
        x += y
        return x

    return add


if __name__ == '__main__':
    f = adder(10)
    print(f(3))
    print(f(5))

    f = adder(13)
    print(f(-3))
    print(f(-5))
