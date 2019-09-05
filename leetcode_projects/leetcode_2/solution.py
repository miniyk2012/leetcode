from leetcode_projects.tree import ListNode
from leetcode_projects.tree import construct_list, destruct_listnode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        ret = cur = None
        p1, p2 = l1, l2
        pre_increment = 0
        while p1 and p2:
            pre_increment, val = divmod(p1.val + p2.val + pre_increment, 10)
            if ret:
                cur.next = ListNode(val)
                cur = cur.next
            else:
                cur = ret = ListNode(val)
            p1, p2 = p1.next, p2.next
        while p1:
            pre_increment, val = divmod(p1.val + pre_increment, 10)
            cur.next = ListNode(val)
            cur = cur.next
            p1 = p1.next
        while p2:
            pre_increment, val = divmod(p2.val + pre_increment, 10)
            cur.next = ListNode(val)
            cur = cur.next
            p2 = p2.next
        if pre_increment == 1:
            cur.next = ListNode(pre_increment)
        return ret


def test():
    # [5] + [5] = [0, 1]
    l1, l2 = construct_list([5]), construct_list([5])
    s = Solution()
    ret = s.addTwoNumbers(l1, l2)
    assert destruct_listnode(ret) == [0, 1]

    # [2,4,3] + [5,6,4] = [7, 0, 8]
    l1, l2 = construct_list([2, 4, 3]), construct_list([5, 6, 4])
    ret2 = s.addTwoNumbers(l1, l2)
    assert destruct_listnode(ret2) == [7, 0, 8]


if __name__ == "__main__":
    test()
