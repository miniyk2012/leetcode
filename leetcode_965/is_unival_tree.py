from tree import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        root_val = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != root_val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

    def isUnivalTree2(self, root: TreeNode) -> bool:
        values = every(root)
        first_val = next(values)
        for val in values:
            if first_val != val:
                return False
        return True


def every(node: TreeNode):
    if node:
        yield node.val
        yield from every(node.left)
        yield from every(node.right)
