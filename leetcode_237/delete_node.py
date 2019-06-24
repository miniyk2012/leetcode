from tree import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        temp = node.next
        node.next = temp.next
        temp.next = None

