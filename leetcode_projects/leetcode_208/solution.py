class Node:
    SIZE = 26

    def __init__(self):
        self.children = [None] * Node.SIZE
        self.is_end_of_node = False


def get_idx(c):
    return ord(c) - ord('a')


def get_char(idx):
    return chr(idx + ord('a'))


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root: Node = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for no, c in enumerate(word):
            idx = get_idx(c)
            if current.children[idx] is None:
                current.children[idx] = Node()
            current = current.children[idx]

        current.is_end_of_node = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        try:
            end = self._travser(word)
            return end.is_end_of_node
        except RuntimeError:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        try:
            self._travser(prefix)
            return True
        except RuntimeError:
            return False

    def _travser(self, word: str) -> Node:
        current = self.root
        for c in word:
            idx = get_idx(c)
            if current.children[idx] is None:
                raise RuntimeError
            current = current.children[idx]
        return current


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
    assert not trie.startsWith("appx")
    assert trie.search("apple")

