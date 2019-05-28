from tree import ListNode
from typing import Tuple


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre = head
        cur = head.next
        while cur:
            old_cur_next = cur.next
            head, pre = self.insert_ahead(head, cur, pre)
            cur = old_cur_next
        return head

    def insert_ahead(self, head, cur, pre) -> Tuple[ListNode, ListNode]:
        """将cur插入到正确的位置上, 返回新的head"""
        visit, visit.next = self, head
        if cur.val < head.val:
            new_head = cur
        else:
            new_head = head
        while visit.next != cur and visit.next.val <= cur.val:
            visit = visit.next
        if visit.next == cur:
            return new_head, cur
        visit.next, cur.next, pre.next = cur, visit.next, cur.next
        return new_head, pre


def print_l(head: ListNode):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    l = ListNode(-2)
    l.next = ListNode(-2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(5)
    l.next.next.next.next = ListNode(30)
    print_l(l)
    print()
    s = Solution()
    l = s.insertionSortList(l)
    print_l(l)
