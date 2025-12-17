from operator import itemgetter
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=itemgetter(0))
        result = []
        if not sorted_intervals:
            return result
        pre = sorted_intervals[0]
        for i in range(1, len(sorted_intervals)):
            if pre[1] >= sorted_intervals[i][0] and pre[1] <= sorted_intervals[i][1]:
                pre = [pre[0], sorted_intervals[i][1]]
            elif pre[1] < sorted_intervals[i][1]:
                result.append(pre)
                pre = sorted_intervals[i]
        result.append(pre)
        return result