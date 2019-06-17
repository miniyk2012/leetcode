from tree import TreeNode, construct_tree
from typing import List, Tuple
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        ret = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            ret.append((node.val, level))
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return self.construct_order(ret)

    def construct_order(self, l: List[(Tuple[int, int])]) -> List[List[int]]:
        ret = []
        level = 0
        level_ret = []
        for val, current_level in l:
            if current_level == level:
                level_ret.append(val)
            else:
                level += 1
                ret.append(level_ret)
                level_ret = [val]
        if level_ret:
            ret.append(level_ret)
        return ret

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """BFS的时候每一层都扫描完，这是更好的方法"""
        if root is None:
            return []
        ret = []
        queue = deque([root])
        while queue:
            this_level = []
            new_level = []
            while queue:  # BFS的时候每一层都扫描完
                first = queue.popleft()
                if first.left:
                    new_level.append(first.left)
                if first.right:
                    new_level.append(first.right)
                this_level.append(first.val)
            ret.append(this_level)
            queue.extend(new_level)
        return ret

    def levelOrder3(self, root: TreeNode) -> List[List[int]]:
        """DFS"""
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, root: TreeNode, level: int):
        if not root:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(root.val)
        self._dfs(root.left, level + 1)
        self._dfs(root.right, level + 1)


if __name__ == '__main__':
    tree = construct_tree([3, 9, 20, None, None, 15, 7])
    s = Solution()
    ret = s.levelOrder3(tree)
    print(ret)
