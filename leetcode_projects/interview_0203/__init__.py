from leetcode_projects.tree import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.next = next_node.next
        node.val = next_node.val
        next_node.next = None