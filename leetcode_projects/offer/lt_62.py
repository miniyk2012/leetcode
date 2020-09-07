class Node:
    def __init__(self, val):
        self.val = val
        self.next_p = None
        self.delete = False


class Solution:
    def lastRemaining2(self, n: int, m: int) -> int:
        """不删除节点, 而是标记为删除, 每次都需要循环找到下个节点, 会超时"""
        root = self.build_linked_list(n)
        node = Node(None)
        node.next_p = root
        total_deleted = 0

        while total_deleted < n:
            this_round = 1
            node = self.next_node(node)
            while this_round < m:
                if not node.delete:
                    this_round += 1
                node = self.next_node(node)
            node.delete = True
            total_deleted += 1
        return node.val

    def next_node(self, node):
        node = node.next_p
        while node.delete:
            node = node.next_p
        return node

    def build_linked_list(self, n):
        root = Node(0)
        pre = root
        for i in range(1, n):
            node = Node(i)
            pre.next_p = node
            pre = node
        pre.next_p = root
        return root

    def lastRemaining(self, n: int, m: int) -> int:
        """用list模拟环, 且每次都删除节点, 下个节点直接取模得到, 勉强做到不超时"""
        l = []
        for i in range(n):
            l.append(i)
        idx = 0
        while n > 1:
            idx = (idx + m - 1) % n
            l.pop(idx)
            n -= 1
        return l[0]


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(5, 3))
    print(s.lastRemaining(10, 17))
