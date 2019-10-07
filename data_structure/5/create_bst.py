from loguru import logger

from leetcode_projects.tree import TreeNode


def insert(root, num):
    if root is None:
        return TreeNode(num)
    if num <= root.val:
        root.left = insert(root.left, num)  # 更新左节点
    else:
        root.right = insert(root.right, num)
    return root


def create_binary_search_tree(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root


def inorder(root):
    if root is None:
        return
    yield from inorder(root.left)
    yield root.val
    yield from inorder(root.right)


def test_create_tree():
    nums = [3, 4, 5, 7, 1, 2]
    root = create_binary_search_tree(nums)
    logger.info(list(inorder(root)))
    assert list(inorder(root)) == [1, 2, 3, 4, 5, 7]
