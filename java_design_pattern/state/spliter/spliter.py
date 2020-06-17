from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Spliter:
    constant: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    _word: str = ''

    @property
    def word(self) -> str:
        return self._word

    @word.setter
    def word(self, word: str):
        self._word = word

    def __init__(self, state: State) -> None:
        self.transition_to(state)
        self.word_list: List[str] = []

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def add_word(self, word):
        self.word_list.append(word)

    """
    The Context delegates part of its behavior to the current State object.
    """

    def split(self, target) -> List[str]:
        for character in target:
            self._state.handle(character)
        return self.word_list


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Spliter:
        return self._context

    @context.setter
    def context(self, context: Spliter) -> None:
        self._context = context

    @abstractmethod
    def handle(self, character: str):
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class ContractionState(State):
    def handle(self, character: str):
        if character in self._context.constant:
            self.context.word += character
            self.context.transition_to(WordState())
        else:
            self.context.add_word(self.context.word[:-1])
            self.context.word = ''
            self.context.transition_to(InitState())


class InitState(State):
    def handle(self, character: str):
        if character in self.context.constant:
            self.context.word += character
            self.context.transition_to(WordState())


class WordState(State):
    def handle(self, character: str):
        if character in self._context.constant:
            self.context.word += character
        elif character == "'":
            self.context.word += "'"
            self.context.transition_to(ContractionState())
        else:
            self.context.add_word(self.context.word)
            self.context.word = ''
            self.context.transition_to(InitState())


if __name__ == '__main__':
    spliter = Spliter(InitState())
    sentence = '''I'm kingname, you should say: "Kingname Oba, 
                          I always remember your motto: 'kingname's genius'" to me, won't you?'''
    print(spliter.split(sentence))
