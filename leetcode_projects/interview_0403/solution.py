from typing import List

from leetcode_projects.tree import TreeNode, ListNode


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        result = []
        if tree is None:
            return result
        queue = [tree]
        while queue:
            num = len(queue)
            head, current = None, None
            for _ in range(num):
                tree_node = queue.pop(0)
                if tree_node.left:
                    queue.append(tree_node.left)
                if tree_node.right:
                    queue.append(tree_node.right)
                new_node = ListNode(tree_node.val)
                if head is None:
                    head = new_node
                else:
                    current.next = new_node
                current = new_node
            result.append(head)
        return result


if __name__ == '__main__':
    pass