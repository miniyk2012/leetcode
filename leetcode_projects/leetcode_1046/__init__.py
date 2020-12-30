import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            if y > x:
                stones.append(y - x)
            stones.sort()
        return 0 if not stones else stones[0]

    def lastStoneWeight2(self, stones: List[int]) -> int:
        max_stones = []
        for x in stones:
            heapq.heappush(max_stones, -x)
        while len(max_stones) > 1:
            y = - heapq.heappop(max_stones)
            x = - heapq.heappop(max_stones)
            if y > x:
                heapq.heappush(max_stones, x - y)
        return 0 if not max_stones else -max_stones[0]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    s = Solution()
    assert s.lastStoneWeight(stones.copy()) == 1
    assert s.lastStoneWeight2(stones) == 1
