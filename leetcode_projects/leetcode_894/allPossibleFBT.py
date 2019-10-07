
from typing import List

from leetcode_projects.tree import TreeNode


class Solution:
    all_tree = {}
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.all_tree:
            return self.all_tree[N]
        ans = []
        if N % 2 == 0 or N < 0:
            return ans
        if N == 1:
            ans = self.all_tree[N] = [TreeNode(0)]
            return ans
        for i in range(0, N):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N - i - 1)
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left, root.right = l, r
                    ans.append(root)
        self.all_tree[N] = ans
        return ans

if __name__ == "__main__":
    s = Solution()
    ret = s.allPossibleFBT(7)
    print(ret)