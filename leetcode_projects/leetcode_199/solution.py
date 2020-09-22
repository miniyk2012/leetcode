from typing import List

from collections import deque
from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = deque([root])
        ret = []
        while stack:
            size = len(stack)
            ret.append(stack[0].val)
            for _ in range(size):
                node = stack.popleft()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return ret


if __name__ == '__main__':
    l = [1, 2, 3, None, 5, None, 4]
    tree = construct_tree(l)
    s = Solution()
    ret = s.rightSideView(tree)
    assert ret == [1, 3, 4]
