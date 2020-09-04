from typing import List
from collections import deque

from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    """深度优先遍历"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        if not root:
            return self.paths
        current_path = str(root.val)
        self.traverse(root, current_path)
        return self.paths

    def traverse(self, node, current_path):
        if node.left:
            path = current_path + '->' + str(node.left.val)
            self.traverse(node.left, path)
        if node.right:
            path = current_path + '->' + str(node.right.val)
            self.traverse(node.right, path)
        if not (node.left or node.right):
            self.paths.append(current_path)


class Solution2:
    """广度优先遍历"""

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        if not root:
            return paths
        node_deque = deque([root])
        path_deque = deque([str(root.val)])
        while node_deque:
            node = node_deque.popleft()
            path = path_deque.popleft()
            if not (node.left or node.right):
                paths.append(path)
                continue
            if node.left:
                node_deque.appendleft(node.left)
                path_deque.appendleft(path + '->' + str(node.left.val))
            if node.right:
                node_deque.appendleft(node.right)
                path_deque.appendleft(path + '->' + str(node.right.val))
        return paths


if __name__ == '__main__':
    l = [1, 2, 3, None, 5]
    root = construct_tree(l)
    solution = Solution()
    paths = solution.binaryTreePaths(root)
    for path in paths:
        print(path)
    print()
    solution2 = Solution2()
    paths2 = solution2.binaryTreePaths(root)
    for path2 in paths2:
        print(path2)
