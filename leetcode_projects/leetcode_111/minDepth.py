from collections import deque

from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.min = None
        self._dfs(root, 0)
        return self.min

    def _dfs(self, node: TreeNode, level: int):
        """使用DFS, 遇到叶子节点, 才决定是否要更新min"""
        if not (node.left or node.right):
            if self.min is None or self.min > level + 1:
                self.min = level + 1
        if node.left:
            self._dfs(node.left, level + 1)
        if node.right:
            self._dfs(node.right, level + 1)

    def minDepth2(self, root: TreeNode) -> int:
        """使用BFS, 遇到叶子节点, 才决定是否要更新min"""
        if root is None:
            return 0
        self.min = None
        self._bfs(root)
        return self.min

    def _bfs(self, node: TreeNode):
        queue = deque([node])
        level = 0
        while queue:
            level += 1
            q_len = len(queue)
            # print(q_len)
            for _ in range(q_len):  # 遍历完一层
                top = queue.popleft()
                if top.left is None and top.right is None:
                    self.min = level  # 因为level是不断上升的, 因此头一个发现的叶子肯定是层数最低的
                    return
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)


if __name__ == '__main__':
    tree = construct_tree([3, 9, 20, None, None, 15, 7, 4, 5, 45, 12])
    s = Solution()
    assert s.minDepth2(tree) == 2
    tree = construct_tree([1, 2])
    assert s.minDepth2(tree) == 2
    tree = construct_tree([1, None, 2])
    assert s.minDepth2(tree) == 2