from collections import deque

from leetcode_projects.tree import TreeNode, construct_tree, bfs_visit_tree


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """BFS"""
        if t1 is None:
            return t2
        elif t2 is None:
            return t1
        stack1 = deque([t1])
        stack2 = deque([t2])
        head = TreeNode(t1.val + t2.val)
        stack3 = deque([head])
        while stack1:
            node1 = stack1.popleft()
            node2 = stack2.popleft()
            node3 = stack3.popleft()

            if node1.left is None:
                node3.left = node2.left
            elif node2.left is None:
                node3.left = node1.left
            else:
                stack1.append(node1.left)
                stack2.append(node2.left)
                left = TreeNode(node1.left.val + node2.left.val)
                node3.left = left
                stack3.append(left)

            if node1.right is None:
                node3.right = node2.right
            elif node2.right is None:
                node3.right = node1.right
            else:
                stack1.append(node1.right)
                stack2.append(node2.right)
                right = TreeNode(node1.right.val + node2.right.val)
                node3.right = right
                stack3.append(right)
        return head

e
if __name__ == '__main__':
    s = Solution()
    l1 = [1, 3, 2, 5]
    l2 = [2, 1, 3, None, 4, None, 7]
    t1 = construct_tree(l1)
    t2 = construct_tree(l2)
    t = s.mergeTrees2(t1, t2)
    print(bfs_visit_tree(t))
