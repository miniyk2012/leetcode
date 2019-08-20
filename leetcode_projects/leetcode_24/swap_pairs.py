from leetcode_projects.tree import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            first, second = pre.next, pre.next.next
            pre.next, first.next, second.next = second, second.next, first
            pre, pre.next = first, first.next
        return self.next


