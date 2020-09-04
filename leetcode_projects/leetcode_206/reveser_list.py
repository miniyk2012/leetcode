from leetcode_projects.tree import ListNode, construct_list, destruct_listnode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


class Solution2:
    """递归实现"""

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        tmp = head.next
        new_head = self.reverseList(tmp)
        tmp.next = head
        head.next = None
        return new_head


class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        """背诵哟"""
        pre, cur = None, head
        while cur:
            tmp = pre
            pre = cur
            cur = cur.next
            pre.next = tmp
        return pre


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    head = construct_list(l)
    s2 = Solution2()
    print(destruct_listnode(s2.reverseList(head)))

    l = [1, 2, 3, 4, 5]
    head = construct_list(l)
    s3 = Solution3()
    print(destruct_listnode(s3.reverseList(head)))
