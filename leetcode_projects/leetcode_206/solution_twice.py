from leetcode_projects.tree import ListNode, construct_list, destruct_listnode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nx = cur.next
            cur.next = pre
            pre = cur
            cur = nx
        return pre