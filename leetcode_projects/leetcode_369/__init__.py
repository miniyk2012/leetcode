from leetcode_projects.tree import ListNode


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        cur = head
        total = 0
        while cur:
            total = 10 * total + cur.val
            cur = cur.next
        total += 1
        tail = None
        while total:
            total, remain = divmod(total, 10)
            tail = ListNode(remain, tail)
        return tail
