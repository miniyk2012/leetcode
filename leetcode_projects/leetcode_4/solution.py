from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        number = len(nums1) + len(nums2)
        mid, remainder = divmod(number, 2)
        elapse_num = 0
        while elapse_num < mid:
            mid_value = self.pop_smaller(nums1, nums2)
            elapse_num += 1
        if remainder == 0:
            return (self.pop_smaller(nums1, nums2) + mid_value) / 2.0
        else:
            return self.pop_smaller(nums1, nums2)

    def pop_smaller(self, s1, s2):
        if s1 and s2:
            if s1[0] > s2[0]:
                return s2.pop(0)
            else:
                return s1.pop(0)
        elif s1:
            return s1.pop(0)
        else:
            return s2.pop(0)


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([0, 0], [0, 0]))
    print(s.findMedianSortedArrays([], [1]))
    print(s.findMedianSortedArrays([2], []))
    print(s.findMedianSortedArrays([1, 3], [2]))
