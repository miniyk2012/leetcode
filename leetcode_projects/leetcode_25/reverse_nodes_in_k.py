from leetcode_projects.tree import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        old_last = self
        cur = head
        first_k = True
        while self.has_k_remain(cur, k):
            i = 0
            last = cur
            pre = None
            while i < k:  # 反转k个node
                cur.next, pre, cur = pre, cur, cur.next
                i += 1
            old_last.next = pre
            old_last = last
            if first_k:
                head = pre
                first_k = False
        old_last.next = cur
        return head

    def has_k_remain(self, cur, k):
        i = 0
        temp_cur = cur
        while temp_cur:
            temp_cur = temp_cur.next
            i += 1
            if i >= k:
                return True
        return False

    def has_k_remain(self, cur, k):
        i = 0
        temp_cur = cur
        while temp_cur:
            temp_cur = temp_cur.next
            i += 1
            if i >= k:
                return True
        return False
