from typing import List, Set, Dict


class Solution:
    def __init__(self):
        self._graph: Dict[str, Set[str]] = {}  # 单词: 与它相邻的单词集合
        self._clusters: Dict[str, int] = {}  # 单词: 组号

    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        self._build_graph(pairs)
        self._do_cluster()
        return self._judge_similarity(words1, words2)

    def _judge_similarity(self, words1, words2):
        for first, second in zip(words1, words2):
            if first == second:
                continue
            if (first not in self._graph) or (second not in self._graph):
                return False
            if self._clusters[first] != self._clusters[second]:
                return False
        return True

    def _build_graph(self, pairs: List[List[str]]):
        for first, second in pairs:
            self._graph.setdefault(first, set()).add(second)
            self._graph.setdefault(second, set()).add(first)

    def _do_cluster(self):
        def _dfs(node: str) -> None:
            # 将node所在的联通集内的所有单词记录为同一组
            if node in self._clusters:
                return
            self._clusters[node] = _id
            for nxt in self._graph[node]:
                _dfs(nxt)

        _id = 0
        for word in self._graph:
            _dfs(word)
            _id += 1


def test1():
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
    s = Solution()
    assert s.areSentencesSimilarTwo(words1, words2, pairs)


if __name__ == '__main__':
    test1()
