from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        if len(self.q) < self.k:
            self.q.append(val)
        elif val > self.q[-1]:
            self.q.pop()
            self.q.append(val)
        self.q.sort(reverse=True)
        return self.q[-1]


class KthLargest2:
    """
    使用优先队列
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        return self.heap[0]


if __name__ == '__main__':
    # Your KthLargest object will be instantiated and called as such:
    obj = KthLargest2(2, [0])
    param_1 = obj.add(-1)
    param_2 = obj.add(1)
    print(param_1)
    print(param_2)
