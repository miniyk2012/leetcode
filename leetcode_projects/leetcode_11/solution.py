from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        area = 0
        while i < j:
            current = min(height[i], height[j]) * (j - i)
            if area < current:
                area = current
            if height[i] < height[j]:
                while i<j:
                    i += 1
                    if height[i-1] < height[i]:
                        break
            else:
                while i<j:
                    j -= 1
                    if height[j] > height[j+1]:
                        break
        return area
