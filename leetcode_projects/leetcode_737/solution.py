from typing import List, Set, Dict


class Solution:
    def __init__(self):
        self._graph: Dict[str, Set[str]] = {}

    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        self._build_graph(pairs)
        return self._judge_similarity(words1, words2)

    def _judge_similarity(self, words1, words2):
        for first, second in zip(words1, words2):
            if first == second:
                continue
            if (first not in self._graph) or (second not in self._graph):
                return False
            if not self._connected(first, second):
                return False
        return True

    def _connected(self, first, second):
        def _dfs(src, dst):
            """src是否可达dst"""
            if src == dst:
                return True
            for nxt in self._graph[src]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                if _dfs(nxt, dst):
                    return True
            return False

        visited = set([first])
        return _dfs(first, second)

    def _build_graph(self, pairs: List[List[str]]):
        for first, second in pairs:
            self._graph.setdefault(first, set()).add(second)
            self._graph.setdefault(second, set()).add(first)


def test1():
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
    s = Solution()
    assert s.areSentencesSimilarTwo(words1, words2, pairs)


if __name__ == '__main__':
    test1()
