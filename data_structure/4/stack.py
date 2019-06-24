class Stack:
    def __init__(self):
        self.data = []
    
    
    def length(self):
        return len(self.data)

    def peek(self):
        if self.data:
            return self.data[-1]
        raise Exception('stack is empty')

    def push(self, ele):
        self.data.append(ele)

    def pop(self):
        if self.data:
            return self.data.pop()
        raise Exception('stack is empty')
    
if __name__ == "__main__":
    s = Stack()
    assert s.length() == 0
    s.push(1)
    s.push(2.5)
    assert s.peek() == 2.5
    assert s.length() == 2
    assert s.pop() == 2.5
    assert s.length() == 1