from collections import defaultdict
from typing import List, Optional

from leetcode_projects.tree import ListNode

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        val_node_map = defaultdict(list)
        for l in lists:
            if l is None:
                continue
            heapq.heappush(h, l.val)
            val_node_map[l.val].insert(0, l)
        dummy = ListNode(0)
        current = dummy
        while h:
            val = heapq.heappop(h)
            node = val_node_map[val].pop()
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(h, node.next.val)
                val_node_map[node.next.val].insert(0, node.next)
        head = dummy.next
        dummy.next = None
        return head