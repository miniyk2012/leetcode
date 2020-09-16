"""https://leetcode-cn.com/problems/min-stack-lcci/"""

from collections import deque


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.sorted_queue = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.sorted_queue or self.sorted_queue[0] >= x:
            self.sorted_queue.appendleft(x)

    def pop(self) -> None:
        ans = self.stack.pop()
        if ans == self.sorted_queue[0]:
            self.sorted_queue.popleft()
        return ans

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_queue[0]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    print(obj.pop())
    print(obj.top())
    print(obj.getMin())
