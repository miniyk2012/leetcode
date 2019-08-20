
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        for i in range(1, target + 1):
            for j in candidates:
                if i == j:
                    dp[i].append([j])
                elif i > j:
                    k = i - j  # 类似Two Sum
                    for path in dp[k]:
                        if j < path[-1]:
                            continue  # 剪枝, 且无须排序candidates: 每次只把不小于当前路径中数的候选值加入
                        new_path = path[:]
                        new_path.append(j)
                        dp[i].append(new_path)
        print(f'dp: {dp}')
        return dp[target]


def test():
    def assert_equal_list(l1: List[List[int]], l2: List[List[int]]):
        print(f'l1={l1}\nl2={l2}')
        assert len(l1) == len(l2)
        assert set(tuple(e) for e in l1) == set(tuple(e) for e in l2)
        print()

    s = Solution()

    candidates = [2, 3, 6, 7]
    target = 7
    expected = [
        [7],
        [2, 2, 3]
    ]
    assert_equal_list(s.combinationSum(candidates, target), expected)

    candidates = [2, 3, 5]
    target = 8
    expected = [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
    assert_equal_list(s.combinationSum(candidates, target), expected)

    candidates = [8, 7, 4, 3]
    target = 11
    expected = [
        [3, 4, 4],
        [3, 8],
        [4, 7]
    ]
    assert_equal_list(s.combinationSum(candidates, target), expected)


if __name__ == '__main__':
    test()
