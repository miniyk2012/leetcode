from typing import Union, Optional, Callable, Generator, Any

Num = Union[int, float]


class Tree:
    """
    Binary search Tree
    """

    def __init__(self, v: Num):
        self.val = v
        self.left: Optional[Tree] = None
        self.right: Optional[Tree] = None

    def add(self, val: Num):
        if val >= self.val:
            if not self.right:
                self.right = Tree(val)
            else:
                self.right.add(val)
        else:
            if not self.left:
                self.left = Tree(val)
            else:
                self.left.add(val)

    def in_order(self, f: Callable) -> None:
        if self.left:
            self.left.in_order(f)
        f(self.val)
        if self.right:
            self.right.in_order(f)

    def pre_order(self, f: Callable) -> None:
        f(self.val)
        if self.left:
            self.left.pre_order(f)
        if self.right:
            self.right.pre_order(f)

    def post_order(self, f: Callable) -> None:
        if self.left:
            self.left.post_order(f)
        if self.right:
            self.right.post_order(f)
        f(self.val)

    def in_order_g(self) -> Generator:
        if self.left:
            yield from self.left.in_order_g()
        yield self.val
        if self.right:
            yield from self.right.in_order_g()

    def post_order_g(self) -> Generator:
        if self.left:
            yield from self.left.post_order_g()
        if self.right:
            yield from self.right.post_order_g()
        yield self.val

    def pre_order_g(self) -> Generator:
        yield self.val
        if self.left:
            yield from self.left.pre_order_g()
        if self.right:
            yield from self.right.pre_order_g()

    def traverse(self) -> Generator:
        smaller = yield self.val
        if smaller and self.left:
            yield from self.left.traverse()
        elif (not smaller) and self.right:
            yield from self.right.traverse()

    def sum(self) -> Num:
        s = 0

        def add(v):
            nonlocal s
            s += v

        self.pre_order(add)
        return s

    def product(self):
        s = 1

        def product(v):
            nonlocal s
            s *= v

        self.pre_order(product)
        return s

    def reduce(self, reducer: Callable[[Num, Num], Num]) -> Num:
        g = self.pre_order_g()
        s = next(g)
        for v in g:
            s = reducer(s, v)
        return s

    def map(self, mapper: Callable[[Num], Num]) -> Generator:
        for v in self.pre_order_g():
            yield mapper(v)

    def slow_contains(self, val: Num) -> bool:
        for v in self.pre_order_g():
            if v == val:
                return True
        return False

    def contains(self, val: Num) -> bool:
        g: Generator = self.traverse()
        v = next(g)
        try:
            while True:
                if v == val:
                    return True
                elif v > val:
                    v = g.send(True)  # 遍历左子树
                else:
                    v = g.send(False)
        except StopIteration:
            return False


if __name__ == '__main__':
    t = Tree(0)
    t.add(1)
    t.add(-2)
    t.add(3)
    t.add(2)

    """
        0
       /  \ 
    -2      1
              \
                3
               /
              2 
    """
    t.pre_order(print)
    print()
    for v in t.pre_order_g():
        print(v)
    print(f'sum={t.sum()}')
    ans = t.reduce(lambda a, b: a + b)
    print(f'sum={ans}')

    print(f'product={t.product()}')
    ans = t.reduce(lambda a, b: a * b)
    print(f'product={ans}')

    values = t.map(lambda x: 2 * x)
    for v in values:
        print(v)
    print(t.slow_contains(1))
    print(t.slow_contains(3))
    print(t.slow_contains(1.2))

    print(f'quick contain 1: {t.contains(1)}')
    print(f'quick contain 0: {t.contains(0)}')
    print(f'quick contain 3: {t.contains(3)}')
    print(f'quick contain 3.3: {t.contains(3.3)}')
    print(f'quick contain 2: {t.contains(2)}')
    print(f'quick contain 1.2: {t.contains(1.2)}')
    print(f'quick contain -1: {t.contains(-1)}')
