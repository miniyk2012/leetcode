from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pass
            

def test():
    matrix = [
        [1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    s = Solution()
    assert s.kthSmallest(matrix, k) == 13


if __name__ == "__main__":
    test()
