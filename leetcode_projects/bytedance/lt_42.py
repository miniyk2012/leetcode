from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """基本思想是把可以取到的水都取到"""
        if not height:
            return 0
        stack = [height[0]]
        total = 0
        for i in range(1, len(height)):
            cur_val = height[i]
            if cur_val <= stack[-1]:
                stack.append(cur_val)
                continue
            # 这一个柱子会把小于cur_val的全部吞掉, 保证stack中的柱子一定是单调递减的
            this_round_water = 0
            if cur_val > stack[0]:
                this_round_water = sum(stack[0] - v for v in stack)
                stack.clear()
                stack.append(cur_val)
                total += this_round_water
                continue
            pop_list, append_list = [], []
            while stack and cur_val > stack[-1]:
                pop_list.append(stack.pop(-1))
                append_list.append(cur_val)
            stack.extend(append_list)
            this_round_water = sum(cur_val - v for v in pop_list)
            total += this_round_water
            stack.append(cur_val)
        return total


if __name__ == '__main__':
    input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(input))
    input = [2, 1, 0, 2]
    print(s.trap(input))
