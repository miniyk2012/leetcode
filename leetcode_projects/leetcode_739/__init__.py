from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        lessno_for_idx = {idx: 0 for idx in range(len(T))}
        ret = [0] * len(T)
        for idx, num in enumerate(T):
            pass
