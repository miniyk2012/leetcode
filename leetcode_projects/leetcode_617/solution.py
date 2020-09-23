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


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 3, 2, 5]
    l2 = [2, 1, 3, None, 4, 7]
    t1 = construct_tree(l1)
    t2 = construct_tree(l2)
    t = s.mergeTrees(t1, t2)
    print(bfs_visit_tree(t))
