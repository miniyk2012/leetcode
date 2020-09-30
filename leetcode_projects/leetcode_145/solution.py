from typing import List

from leetcode_projects.tree import TreeNode

from collections import deque
class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """递归做法"""
        self.ret = []
        self.visit(root)
        return self.ret

    def visit(self, node):
        if node is None:
            return
        self.visit(node.left)
        self.visit(node.right)
        self.ret.append(node.val)


    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """迭代实现"""
        ret = []
        if not root:
            return ret
        stack = deque([root])
        while stack:
            top = stack[0]
            if top.left:
                stack.appendleft(top.left)
                continue
            if top.right:
                stack.appendleft(top.right)
                continue
            stack.popleft()
            ret.append(top.val)
        return ret


if __name__ == '__main__':
    root = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    root.right = two
    two.left = three
    s = Solution()
    print(s.postorderTraversal1(root))
    print(s.postorderTraversal(root))