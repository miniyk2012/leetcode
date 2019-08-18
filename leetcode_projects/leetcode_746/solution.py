from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return min(cost)
        dp_cost = [0] * (len(cost))
        dp_cost[0], dp_cost[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp_cost[i] = min(dp_cost[i - 1], dp_cost[i - 2]) + cost[i]
        return min(dp_cost[-1], dp_cost[-2])


def test():
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


if __name__ == '__main__':
    test()
