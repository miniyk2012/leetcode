from typing import Optional

from leetcode_projects.tree import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        for i in range(n-1):
            right = right.next
        while right and right.next:
            right = right.next
            left = left.next
        temp = left.next
        left.next = temp.next
        temp.next = None
        head = dummy.next
        dummy.next = None
        return head
