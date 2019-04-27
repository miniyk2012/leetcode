from dataclasses import dataclass, field
from typing import Set, List


@dataclass(unsafe_hash=True, order=True)
class Item:
    prize: int
    amount: int = field(hash=False, compare=False)

    def __post_init__(self):
        self.prize = int(self.prize)

    def to_list(self):
        return [str(self.prize), self.amount]


class Container:

    def __init__(self):
        self.items: Set[Item] = set()

    def add(self, item: Item) -> None:
        self.items.discard(item)
        if item.amount != 0:
            self.items.add(item)

    def addAll(self, items: List[Item]) -> None:
        for item in items:
            self.items.add(item)

    def to_list(self):
        items = list(sorted(self.items))
        return [item.to_list() for item in items]


def test_data():
    full = [
        ['10', 2],
        ['11', 4],
        ['24', 5]
    ]

    partial = [
        ['10', 6],
        ['24', 0],
        ['25', 5]
    ]

    c = Container()
    items = [Item(*e) for e in full]
    c.addAll(items)
    print(c.to_list())
    for e in partial:
        c.add(Item(*e))
    print(c.to_list())
