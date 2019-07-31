from leetcode_projects.tree import ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        l = []
        cur = head
        while cur:
            l.append(cur.val)
            cur = cur.next
        l.sort()
        ret = cur = ListNode(l[0])
        for e in l[1:]:
            cur.next = ListNode(e)
            cur = cur.next
        return ret
