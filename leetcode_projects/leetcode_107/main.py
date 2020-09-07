from collections import deque
from typing import List

from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def levelOrderBottom2(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([(root, 0)])
        l = []
        while queue:
            node = queue.popleft()
            if node[1] < len(l):
                l[node[1]].append(node[0].val)
            else:
                l.append([node[0].val])
            if node[0].left:
                queue.append((node[0].left, node[1] + 1))
            if node[0].right:
                queue.append((node[0].right, node[1] + 1))
        return l[::-1]

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        l = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            l.append(level)
        return l[::-1]


if __name__ == '__main__':
    l = [3, 9, 20, None, None, 15, 7]
    root = construct_tree(l)
    s = Solution()
    ret = s.levelOrderBottom(root)
    print(ret)
