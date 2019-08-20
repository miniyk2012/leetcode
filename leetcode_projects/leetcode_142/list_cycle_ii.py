from leetcode_projects.tree import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next
        return None
