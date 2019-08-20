"""
https://leetcode-cn.com/problems/merge-k-sorted-lists/submissions/
https://leetcode.com/problems/merge-k-sorted-lists/submissions/
https://www.bilibili.com/video/av44615806/?spm_id_from=333.788.videocard.3
"""

from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h: List[ListNode] = []
        for head in lists:
            node: ListNode = head
            while node:
                h.append(node.val)
                node = node.next
        if not h:
            return None
        heapq.heapify(h)
        root = ListNode(heapq.heappop(h))
        current_node = root
        while h:
            current_node.next = ListNode(heapq.heappop(h))
            current_node = current_node.next
        return root
