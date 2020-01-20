from typing import Iterable, Protocol, List


class SupportsChildren(Protocol):
    def children(self) -> List:
        """"""


class Frame(object):
    def __init__(self, child_widgets):
        self.child_widgets = child_widgets

    def children(self):
        return self.child_widgets


class Label(object):
    def __init__(self, text):
        self.text = text

    def children(self):
        return []


def children_all(items: Iterable[SupportsChildren]) -> None:
    for item in items:
        print(item.children())


if __name__ == '__main__':
    children_all([Label('label'), Frame([Label('sub label')])])  # Okay!
