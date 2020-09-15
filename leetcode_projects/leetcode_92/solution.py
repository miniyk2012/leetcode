from leetcode_projects.tree import ListNode, construct_list, destruct_listnode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        pre = None
        cur = head
        for _ in range(m - 1):
            pre = cur
            cur = cur.next
        mid_head = cur
        mid_pre = None
        for _ in range(n - m + 1):
            mid_pre, cur, mid_pre.next = cur, cur.next, mid_pre
        if pre:
            pre.next = mid_pre
        if mid_head:
            mid_head.next = cur
        if m == 1:
            head = mid_pre
        return head


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    list_node = construct_list(l)
    s = Solution()
    head = s.reverseBetween(list_node, 2, 4)
    print(destruct_listnode(head))
    l = [5]
    list_node = construct_list(l)
    head = s.reverseBetween(list_node, 1, 1)
    print(destruct_listnode(head))

    l = [3, 5]
    list_node = construct_list(l)
    head = s.reverseBetween(list_node, 1, 1)
    print(destruct_listnode(head))

    l = [3, 5]
    list_node = construct_list(l)
    head = s.reverseBetween(list_node, 1, 2)
    print(destruct_listnode(head))
