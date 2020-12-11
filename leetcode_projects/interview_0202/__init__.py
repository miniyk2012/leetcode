from leetcode_projects.tree import ListNode


class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        tail = head
        for _ in range(k):
            tail = tail.next
        cur = head
        while tail:
            tail = tail.next
            cur = cur.next
        return cur.val