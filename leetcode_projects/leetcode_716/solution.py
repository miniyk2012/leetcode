from collections import deque

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.max_stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack:
            max_num = x
        else:
            max_num = max(x, self.max_stack[-1])
        self.max_stack.append(max_num)

    def pop(self) -> int:
        ans = self.stack.pop()
        self.max_stack.pop()
        return ans

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        ans = self.peekMax()
        stack = deque()
        top = self.pop()
        while top < ans:
            stack.append(top)
            top = self.pop()
        while stack:
            self.push(stack.pop())
        return ans

if __name__ == '__main__':
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(6)
    print(s.peekMax())
    print(s.popMax())
    print(s.popMax())