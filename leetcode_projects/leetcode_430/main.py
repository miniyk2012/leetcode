"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        ret = f'[{self.val}]'
        if self.prev:
            try:
                ret = f'{self.prev.val}-' + ret
            except:
                pass
        if self.next:
            try:
                ret = ret + f'-{self.next.val}'
            except:
                pass
        return ret


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        def dfs(pre, cur):
            if cur is None:
                return pre
            end = cur
            pre.next, cur.prev = cur, pre
            child = cur.child
            after = cur.next
            cur.child, cur.next = None, None
            if child:
                end = dfs(cur, child)
            print(cur.child)
            if after:
                after.prev = None
                end = dfs(end, after)
            return end

        pre = Node(None, None, head, None)
        cur = head
        dfs(pre, cur)
        head.prev = None
        return head


if __name__ == '__main__':
    node1 = Node(1, None, None, None)
    node2 = Node(2, None, None, None)
    node3 = Node(3, None, None, None)
    node4 = Node(4, None, None, None)
    node1.next, node2.prev = node2, node1
    node2.next, node3.prev = node3, node2
    node3.next, node4.prev = node4, node3
    s = Solution()
    head = s.flatten(node1)
    while head:
        print('val', head)
        print('prev', head.prev)
        print('child', head.child)
        print('next', head.next)
        head = head.next
