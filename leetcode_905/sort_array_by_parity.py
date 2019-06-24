from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for e in A:
            if e % 2 == 0:
                even.append(e)
            else:
                odd.append(e)
        even.extend(odd)
        return even