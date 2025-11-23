from leetcode_projects.leetcode_155.solution import MinStack


def test_basic():
    obj = MinStack()
    obj.push(5)
    assert obj.top() == 5
    obj.pop()

    obj.push(20)
    obj.push(10)
    obj.push(30)
    assert obj.top() == 30
    assert obj.getMin() == 10
    obj.pop()
    assert obj.getMin() == 10
    assert obj.top() == 10
    obj.pop()
    assert obj.getMin() == 20
    obj.top() == 20
    obj.pop()

