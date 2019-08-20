from leetcode_projects.tree import TreeNode, construct_tree
from collections import deque


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_depth = self.bfs(root)
        return max_depth

    def bfs(self, root: TreeNode):
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                top = queue.popleft()
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
        return level


if __name__ == '__main__':
    tree = construct_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    assert s.maxDepth2(tree) == 3