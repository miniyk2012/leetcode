from leetcode_projects.tree import TreeNode, construct_tree, bfs_visit_tree

from collections import deque
class Solution:
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left, root.right = left, right
        return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = deque([root])
        while stack:
            top = stack.popleft()
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
            top.left, top.right = top.right, top.left
        return root


if __name__ == '__main__':
    l = [4, 2, 7, 1, 3, 6, 9]
    root = construct_tree(l)
    s = Solution()
    new_tree = s.invertTree(root)
    print(bfs_visit_tree(new_tree))