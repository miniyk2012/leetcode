from typing import List
import math


class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        inf = 1e10
        max_temperature = 101
        # next数组记录每个温度的最小下标
        # next[t] = 10 表示温度t的最小下标是10
        next = [inf] * max_temperature
        ret = [0 for _ in range(len(temperatures))]
        # 倒序遍历, 逐步更新next数组
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            if i < next[temp]:
                next[temp] = i  # 更新当前温度的最小下标
            min_index = inf
            for t in range(temp + 1, max_temperature):
                if next[t] < min_index:
                    min_index = next[t]
            if min_index != inf:
                ret[i] = min_index - i
        return ret

    def dailyTemperatures_slow(self, temperatures: List[int]) -> List[int]:
        ret = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures) - 1, -1, -1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ret[i] = j - i
                    break
        return ret
