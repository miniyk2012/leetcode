from leetcode_projects.tree import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = l1
        right = l2
        head, cur = None, None
        next_val = 0
        while True:
            if not (left or right or next_val != 0):
                break
            left_val, right_val = 0, 0
            if left != None:
                left_val = left.val
                left = left.next
            if right != None:
                right_val = right.val
                right = right.next

            next_val, val = divmod(left_val + right_val + next_val, 10)
            node = ListNode()
            node.val = val
            if head is None:
                cur, head = node, node
            else:
                cur.next = node
                cur = node
        return head
