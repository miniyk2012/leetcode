from typing import List, Dict


class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        word_map = self._build_map(pairs)

        return self._judge_similar(word_map, words1, words2)

    def _judge_similar(self, word_map, words1, words2):
        for first, second in zip(words1, words2):
            if first == second:
                continue
            if (first not in word_map) or (second not in word_map):
                return False
            if second not in word_map[first]:
                return False
        return True

    def _build_map(self, pairs: List[List[str]]) -> Dict:
        ret: Dict = {}
        for first, second in pairs:
            ret.setdefault(first, set()).add(second)
            ret.setdefault(second, set()).add(first)
        return ret


def test1():
    word1 = ["great", "acting", "skills"]
    word2 = ["fine", "drama", "talent"]
    pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    s = Solution()
    assert s.areSentencesSimilar(word1, word2, pairs)


if __name__ == '__main__':
    test1()
