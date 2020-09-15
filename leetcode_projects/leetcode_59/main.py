from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue: deque = deque()  # 单调递减
        self.queue2: deque = deque()

    def max_value(self) -> int:
        return self.queue[0] if self.queue else -1

    def push_back(self, value: int) -> None:
        self.queue2.append(value)
        while self.queue and self.queue[-1] < value:
            self.queue.pop()
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue2:
            return -1
        ans = self.queue2.popleft()
        if ans  == self.queue[0]:
            self.queue.popleft()
        return ans