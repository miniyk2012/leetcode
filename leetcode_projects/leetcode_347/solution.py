from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        return [num for num, _ in counter.most_common(k)]
