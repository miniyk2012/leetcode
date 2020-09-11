from typing import List

from leetcode_projects.tree import TreeNode, construct_tree
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return 0
        averages = []
        queue = deque([root])
        while queue:
            average = 0
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                average += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average /= length
            averages.append(average)
        return averages

if __name__ == '__main__':
    l = [3, 9, 0, 15, 7]
    root = construct_tree(l)
    s = Solution()
    print(s.averageOfLevels(root))




