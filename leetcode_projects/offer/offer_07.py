from typing import List

from leetcode_projects.tree import TreeNode, bfs_visit_tree


class Solution:
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        if index > 0:
            left_inorder = inorder[0:index]  # 拷贝太消耗内存, 可以优化为指针
            left_preorder = preorder[1:index + 1]
            head.left = self.buildTree(left_preorder, left_inorder)
        if index < len(inorder) - 1:
            right_inorder = inorder[index + 1:]
            right_preorder = preorder[index + 1:]
            head.right = self.buildTree(right_preorder, right_inorder)
        return head

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        self.preorder = preorder
        self.inorder = inorder
        length = len(preorder)
        return self.build(0, length - 1, 0, length - 1)

    def build(self, start_pre, end_pre, start_in, end_in):
        value = self.preorder[start_pre]
        head = TreeNode(value)
        index = self.inorder.index(value, start_in, end_in + 1)
        left_length = index - start_in
        right_length = end_in - index
        if left_length > 0:
            head.left = self.build(start_pre + 1, start_pre + left_length, start_in, start_in + left_length-1)
        if right_length > 0:
            head.right = self.build(start_pre + left_length + 1, end_pre, index + 1, end_in)
        return head


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s = Solution()
    tree = s.buildTree(preorder, inorder)
    l = bfs_visit_tree(tree)
    print(l)
