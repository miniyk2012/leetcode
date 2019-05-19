class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []  # 假设支持pop(0)和append(x)操作，也就是队列操作
        self.q2 = []  # 假设支持pop(0)和append(x)操作，也就是队列操作
        self.top_value = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)
        self.top_value = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        self._swap_until_left_one()
        ret = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return ret

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_value

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1

    def _swap_until_left_one(self) -> None:
        while len(self.q1) > 1:
            self.top_value = self.q1.pop(0)
            self.q2.append(self.top_value)

