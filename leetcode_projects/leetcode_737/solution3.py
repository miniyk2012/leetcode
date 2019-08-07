"""union find算法"""
from typing import List


class UnionFindSet:
    """并查集类, 只支持所有元素都是整数.
    如果要支持非整数的元素请不要修改该类, 可以通过映射的方式扩展功能"""

    def __init__(self, n: int):
        """支持的元素为0~n-1
        :param n: 最多元素个数
        """
        self._parents: List[int] = [i for i in range(n)]  # _parents[u] = v 表示u的父亲是v
        self._ranks: List[int] = [0] * n  # _ranks[find(u)] = v 表示u所在的连通集rank为v

    def find(self, u: int) -> int:
        """返回num所在连通集的根,
        在遍历的同时make tree flat"""
        if self._parents[u] != u:
            self._parents[u] = self.find(self._parents[u])
        return self._parents[u]

    def union(self, u: int, v: int) -> None:
        """合并u, v所在的连通集"""
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return
        rank_u, rank_v = self._ranks[root_u], self._ranks[root_v]
        if rank_u > rank_v:
            self._parents[root_v] = root_u
        elif rank_u < rank_v:
            self._parents[root_u] = root_v
        else:
            self._parents[root_u] = root_v
            self._ranks[root_v] = rank_v + 1


class Solution:
    NOT_EXIST = -1

    def __init__(self):
        self._word_2_index = {}  # 单词到并查集元素的映射关系

    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        union_find_set = UnionFindSet(len(pairs) * 2)

        for first, second in pairs:
            union_find_set.union(self._get_index(first), self._get_index(second))

        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            idx1, idx2 = self._get_index(word1, False), self._get_index(word2, False)
            if idx1 == Solution.NOT_EXIST or idx2 == Solution.NOT_EXIST:
                return False
            if union_find_set.find(idx1) != union_find_set.find(idx2):
                return False
        return True

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
