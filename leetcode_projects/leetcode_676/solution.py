from typing import List


class MagicDictionary:
    """使用了fuzz的思想来做这道题, build略慢, 但是search非常快, 适合一次build后, 多次search的场景"""
    FUZZ_CHAR = '*'

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = {}

    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in words:
            self._add_word(word)

    def _add_word(self, word: str) -> None:
        for idx in range(len(word)):
            fuzz_word = self._build_fuzz_word(idx, word)
            self._dict.setdefault(fuzz_word, set()).add(word[idx])

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for idx in range(len(word)):
            fuzz_word = self._build_fuzz_word(idx, word)
            if self._exist_fuzz_word(fuzz_word, word[idx]):
                return True
        return False

    def _build_fuzz_word(self, idx, word: str) -> str:
        fuzz_word = word[:idx] + self.FUZZ_CHAR + word[idx + 1:]
        return fuzz_word

    def _exist_fuzz_word(self, fuzz_word: str, origin_char: str) -> bool:
        if fuzz_word not in self._dict:
            return False
        if origin_char in self._dict[fuzz_word] and len(self._dict[fuzz_word]) == 1:
            return False
        return True


def test1():
    magic_dict = MagicDictionary()
    magic_dict.buildDict(["hello", "leetcode"])
    assert not magic_dict.search("hello")
    assert magic_dict.search("hhllo")
    assert not magic_dict.search("hell")
    assert not magic_dict.search("leetcoded")


def test2():
    magic_dict = MagicDictionary()
    magic_dict.buildDict(["hello", "leetcode", "hallo"])
    assert magic_dict.search("hello")
    assert magic_dict.search("hhllo")
    assert not magic_dict.search("hell")
    assert not magic_dict.search("leetcoded")


if __name__ == '__main__':
    test1()
    test2()
