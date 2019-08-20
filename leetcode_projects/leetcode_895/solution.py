from operator import attrgetter
from typing import Dict, List


class FreqStack:

    def __init__(self):
        self._val_freq: Dict[int, int] = {}
        self._freq_stack: Dict[int, List] = {}
        self._max_freq: int = 0

    def push(self, x: int) -> None:
        freq = self._val_freq.setdefault(x, 0) + 1
        self._val_freq[x] = freq
        if freq > self._max_freq:
            self._max_freq = freq
        self._freq_stack.setdefault(freq, []).append(x)

    def pop(self) -> int:
        val = self._freq_stack.get(self._max_freq).pop()
        self._val_freq[val] -= 1
        if self._val_freq[val] == 0:
            self._val_freq.pop(val)
        if len(self._freq_stack.get(self._max_freq)) == 0:
            self._freq_stack.pop(self._max_freq)
            self._max_freq -= 1
        return val


def execute(commands, params, expecteds):
    stack = FreqStack()
    for command, param, expected in zip(commands[1:], params[1:], expecteds[1:]):
        actual = attrgetter(command)(stack)(*param)
        print(f'{command}{param and param[0]}={actual} ?= {expected}')
        assert actual == expected

    print(stack._freq_stack)
    print(stack._val_freq)


def test1():
    commands = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
    params = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
    expected = [None, None, None, None, None, None, None, 5, 7, 5, 4]
    execute(commands, params, expected)


if __name__ == '__main__':
    test1()
