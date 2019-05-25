class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []  # 假设支持pop()和append(x)操作，也就是栈操作
        self.output = []  # 假设支持pop()和append(x)操作，也就是栈操作

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.output:
            return self.output.pop()
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.output:
            return self.output[-1]
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.input and not self.output
