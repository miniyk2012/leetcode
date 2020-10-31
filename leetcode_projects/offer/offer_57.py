from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ret = []
        i, j = 1, 2
        sum_value = 3
        while i <= target // 2:
            if sum_value == target:
                ret.append(list(range(i, j + 1)))
                j += 1
                i += 1
            elif sum_value < target:
                j += 1
                sum_value += j
                continue
            else:
                i += 1
            sum_value = sum(range(i, j + 1))
        return ret


if __name__ == '__main__':
    s = Solution()
    ret = s.findContinuousSequence(15)
    print(ret)
