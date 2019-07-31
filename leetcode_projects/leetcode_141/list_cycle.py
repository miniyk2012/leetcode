from leetcode_projects.tree import ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
