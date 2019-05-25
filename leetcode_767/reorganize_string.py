from collections import defaultdict
import heapq
from math import ceil


class Solution:
    def reorganizeString(self, S: str) -> str:
        m: defaultdict = defaultdict(lambda: 0)
        for s in S:
            m[s] += 1

        q: list = []
        for k, v in m.items():
            heapq.heappush(q, [-v, k])

        if -q[0][0] > ceil(len(S) / 2):
            return ''
        ans = []
        while len(q) >= 2:
            e1 = heapq.heappop(q)
            e2 = heapq.heappop(q)
            ans.extend([e1[1], e2[1]])

            if e1[0] < -1:
                e1[0] += 1
                heapq.heappush(q, e1)
            if e2[0] < -1:
                e2[0] += 1
                heapq.heappush(q, e2)
        assert len(q) <= 1
        if q:
            ans.append(heapq.heappop(q)[1])
        return ''.join(ans)


def test1():
    l = "aab"
    s = Solution()
    print(s.reorganizeString(l))
    l = "aaab"
    print(s.reorganizeString(l))
    l = 'vvvlo'
    print(s.reorganizeString(l))  # == "vlvov"
    l = "baaba"
    print(s.reorganizeString(l))
    l = "sfffp"
    print(s.reorganizeString(l))
    l = "abbabbaaab"
    print(s.reorganizeString(l))
