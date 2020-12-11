from leetcode_projects.tree import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        length = self.get_length(head)
        if length <= 1:
            return head
        k = k % length
        tail = head
        for _ in range(k):
            tail = tail.next
        pre = head
        while tail.next:
            tail = tail.next
            pre = pre.next
        tail.next = head
        head = pre.next
        pre.next = None
        return head

    def get_length(self, head):
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        return length