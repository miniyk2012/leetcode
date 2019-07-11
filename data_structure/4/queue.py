"""用LinkedList实现queue"""

import sys
import os
sys.path.append(os.path.join(os.path.join(os.path.dirname(__file__), '..'), '3'))

import ll

class Queue:

    def __init__(self):
        self.data = ll.LinkedList()

    def length(self):
        return self.data.length()

    def peek(self):
        if not self.data.is_empty():
            return next(self.data.first(1))
        raise Exception('queue is empty, peek failed')

    def put(self, ele):
        self.data.add(ele)

    def get(self):
        if not self.data.is_empty():
            return self.data.pophead()
        raise Exception('queue is empty, get failed')

if __name__ == "__main__":
    q = Queue()
    assert q.length() == 0
    q.put(1)
    assert q.length() == 1
    q.put(2)
    q.put(3)
    assert q.peek() == 1
    assert q.get().v == 1
    assert q.length() == 2
    assert q.get().v == 2
    assert q.get().v == 3
    assert q.length() == 0
    try:
        q.get()
    except Exception as e:
        assert e.args[0] == 'queue is empty, get failed'
    else:
        raise AssertionError
    
    try:
        q.peek()
    except Exception as e:
        assert e.args[0] == 'queue is empty, peek failed'
    else:
        raise AssertionError
    