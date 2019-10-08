from __future__ import annotations

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None

    def __repr__(self):
        return str(self.val)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


LEFT = 'left'
RIGHT = 'right'


def next_side(side):
    if side == LEFT:
        return RIGHT
    return LEFT


def dfs_visit_tree(root: TreeNode):
    l = []
    if root is None:
        return []
    l.append(root.val)
    left_l = dfs_visit_tree(root.left)
    right_l = dfs_visit_tree(root.right)
    return l + left_l + right_l


def dfs_visit_tree2(root):
    stack = [root]
    ret = []
    while True:
        if not stack:
            return ret
        top = stack.pop()
        if top is None:
            continue
        stack.append(top.right)
        stack.append(top.left)
        ret.append(top.val)


def construct_tree(l):
    if not l:
        return None
    root = TreeNode(l[0])
    nodes = [root]
    curr_node = root
    curr_side = LEFT
    for val in l[1:]:
        if val is None:
            setattr(curr_node, curr_side, None)
        else:
            node = TreeNode(val)
            setattr(curr_node, curr_side, node)
            nodes.append(node)
        curr_side = next_side(curr_side)
        if curr_side == LEFT:
            nodes.pop(0)
            curr_node = nodes[0]
    return root


def test_construct_tree():
    l = [1, 2, 3, None, 4, 5, None, None, 6, None, 7]
    root = construct_tree(l)
    new_l = dfs_visit_tree(root)
    print(new_l)
    new_l2 = dfs_visit_tree2(root)
    print(new_l2)


def construct_list(l: List):
    ret = cur = None
    for val in l:
        node = ListNode(val)
        if ret is None:
            ret = cur = node
        else:
            cur.next = node
            cur = cur.next
    return ret


def destruct_listnode(l: ListNode):
    ret = []
    cur = l
    while cur:
        ret.append(cur.val)
        cur = cur.next
    return ret
