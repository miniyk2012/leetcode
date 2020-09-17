from typing import List

from leetcode_projects.tree import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length_list = self.cal_length_list(root, k)
        rets = []
        pre = None
        head = cur = root
        for i in range(k):
            for _ in range(length_list[i]):
                pre, cur = cur, cur.next
            if pre:
                pre.next = None
            rets.append(head)
            head = cur
        return rets

    def list_length(self, root):
        length = 0
        cur = root
        while cur:
            length +=1
            cur = cur.next
        return length

    def cal_length_list(self, root, k):
        length = self.list_length(root)
        n, m = divmod(length, k)
        length_list = [n for _ in range(k)]
        index = 0
        while m:
            length_list[index] += 1
            index += 1
            m -= 1
        return length_list


if __name__ == '__main__':
    pass