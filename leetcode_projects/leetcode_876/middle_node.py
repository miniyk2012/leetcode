from leetcode_projects.tree import ListNode



class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        list_length = self.get_length(head)
        start, mid_node = 0, head
        while start < list_length // 2:
            start += 1
            mid_node = mid_node.next
        return mid_node

    def get_length(self, head):
        list_length, cur = 0, head
        while cur:
            cur = cur.next
            list_length += 1
        return list_length
