from typing import List


# 不排序的写法，只有遇到减到负数的时候剪枝

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = candidates
        self.size = len(candidates)
        if self.size == 0:
            return []

        self.candidates.sort()
        # 在遍历的过程中记录路径，一般而言它是一个栈
        path = []

        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(0, path, target)
        return self.res

    def __dfs(self, begin, path, target):
        res, candidates, size = self.res, self.candidates, self.size
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行（一定要先排序）
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(index, path, residue)
            path.pop()


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
