from collections import deque
from typing import List

from leetcode_projects.tree import TreeNode


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
            top = stack[-1]
            if top.left:
                stack.append(top.left)
                top.left = None  # 清空表示该节点已经处理过左子树, 后续就不用再处理了
            elif top.right:
                stack.append(top.right)
                top.right = None
            else:
                ret.append(top.val)
                stack.pop()
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