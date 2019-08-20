from leetcode_projects.tree import TreeNode, construct_tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            left_max = self.max_in_tree(root.left)
            if root.val <= left_max:
                return False
            if not self.isValidBST(root.left):
                return False
        if root.right:
            right_min = self.min_in_tree(root.right)
            if root.val >= right_min:
                return False
            if not self.isValidBST(root.right):
                return False
        return True

    def min_in_tree(self, node: TreeNode):
        min = node.val
        current = node
        while current.left:
            min = current.left.val
            current = current.left

        return min

    def max_in_tree(self, node: TreeNode):
        max = node.val
        current = node
        while current.right:
            max = current.right.val
            current = current.right
        return max

    def isValidBST2(self, root: TreeNode):
        """
        做一次中序遍历，看是否是升序的
        :param root:
        :return:
        """
        in_order_list = self.in_order_visit(root)
        return in_order_list == list(sorted(set(in_order_list)))  # 如果有重复数字也不是BST

    def in_order_visit(self, node: TreeNode):
        if node is None:
            return []
        return self.in_order_visit(node.left) + [node.val] + self.in_order_visit(node.right)

    def isValidBST3(self, root: TreeNode):
        """
        中序遍历，但是只保存前继节点
        :param root:
        :return:
        """
        self.prev = None
        return self.helper(root)

    def helper(self, node: TreeNode):
        """对树做中序遍历，如果发现不是递增的就返回False，遍历完都递增返回True
        遍历完时self.prev保存最后遍历到的元素"""
        if node is None:
            return True
        if not self.helper(node.left):
            return False
        if self.prev is not None and node.val <= self.prev:
            return False
        self.prev = node.val
        return self.helper(node.right)


if __name__ == '__main__':
    l = [0, None, -1]
    root = construct_tree(l)
    s = Solution()
    print(s.isValidBST3(root))
