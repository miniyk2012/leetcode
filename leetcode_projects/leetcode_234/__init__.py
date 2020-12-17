from leetcode_projects.tree import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        cur = head
        while cur:
            q.append(cur.val)
            cur = cur.next
        return q == q[::-1]
