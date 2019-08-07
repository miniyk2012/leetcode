"""union find算法"""
from typing import List

from leetcode_projects.data_structs import UnionFindSet


class Solution:
    NOT_EXIST = -1

    def __init__(self):
        self._word_2_index = {}  # 单词到并查集元素的映射关系

    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        union_find_set = UnionFindSet(len(pairs) * 2)
        self._union_pairs(pairs, union_find_set)
        return self._judge_similarity(union_find_set, words1, words2)

    def _judge_similarity(self, union_find_set, words1, words2):
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            idx1, idx2 = self._get_index(word1, False), self._get_index(word2, False)
            if idx1 == Solution.NOT_EXIST or idx2 == Solution.NOT_EXIST:
                return False
            if union_find_set.find(idx1) != union_find_set.find(idx2):
                return False
        return True

    def _union_pairs(self, pairs, union_find_set):
        for first, second in pairs:
            union_find_set.union(self._get_index(first), self._get_index(second))

    def _get_index(self, word: str, create=True) -> int:
        """create=True时, 构造单词到并查集元素的映射, 并获得该映射值
        create=False时, 获取先前构造好的映射值, 如果不存在返回NOT_EXIST"""
        if word in self._word_2_index:
            return self._word_2_index[word]
        if not create:
            return Solution.NOT_EXIST
        size = len(self._word_2_index)
        self._word_2_index[word] = size
        return size


def test_union_find_set():
    union_find_set = UnionFindSet(10)
    union_find_set.union(0, 2)
    union_find_set.union(2, 4)
    union_find_set.union(4, 9)
    assert union_find_set.find(0) == union_find_set.find(9)
    assert union_find_set.find(0) == union_find_set.find(2)
    assert union_find_set.find(0) == union_find_set.find(4)
    assert union_find_set.find(2) == union_find_set.find(9)
    assert union_find_set.find(7) != union_find_set.find(9)
    assert union_find_set.find(7) != union_find_set.find(8)


def test1():
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "painting", "talent"]
    pairs = [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]
    s = Solution()
    assert not s.areSentencesSimilarTwo(words1, words2, pairs)


def test2():
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["drama", "acting"], ["skills", "talent"]]
    s = Solution()
    assert s.areSentencesSimilarTwo(words1, words2, pairs)


if __name__ == '__main__':
    test_union_find_set()
    test1()
    test2()
