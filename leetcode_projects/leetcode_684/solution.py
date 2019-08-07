from typing import List

from leetcode_projects.data_structs import UnionFindSet


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find_set = UnionFindSet(len(edges) + 1)

        for node1, node2 in edges:
            # 已经联通的节点不能再次联通，肯定是多余的边，因为只有n条边，因此最多也就1条多余的边，因此可知这也是最后那条多余的边
            if union_find_set.find(node1) == union_find_set.find(node2):
                return [node1, node2]
            union_find_set.union(node1, node2)


def test1():
    s = Solution()
    assert s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


if __name__ == '__main__':
    test1()
