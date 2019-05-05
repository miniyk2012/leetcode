from typing import Union, Optional, Callable

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
            self.left.in_order(f)
        if self.right:
            self.right.in_order(f)

    def post_order(self, f: Callable) -> None:
        if self.left:
            self.left.in_order(f)
        if self.right:
            self.right.in_order(f)
        f(self.val)


if __name__ == '__main__':
    t = Tree(0)
    t.add(-1)
    t.add(-2)
    t.add(1)
    t.add(2)
    t.post_order(lambda v: print(v))
