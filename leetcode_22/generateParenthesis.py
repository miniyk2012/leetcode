from typing import List

memo = {0: [''],
        1: ['()']}


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = set()
        if n in memo:
            return memo[n]
        for left_num in range(0, n - 1):
            left = self.generateParenthesis(left_num)
            right = self.generateParenthesis(n - 1 - left_num)
            for left_p in left:
                for right_p in right:
                    ret.add('(' + left_p + ')' + right_p)
                    ret.add(left_p + '()' + right_p)
                    ret.add('()' + left_p + right_p)
                    ret.add(left_p + right_p + '()')
                    ret.add(left_p + '(' + right_p + ')')
                    ret.add('(' + left_p + right_p + ')')
        ret = list(ret)
        memo[n] = ret
        return ret

    def generateParenthesis2(self, n: int) -> List[str]:
        self.list = []
        self._gen(0, 0, n, '')
        return self.list

    def _gen(self, left, right, n, result):
        """
        生成n对括号，并保存到self.list中, 一个一个按顺序往结果中添加
        :param left: 当前用了几个左括号
        :param right: 当前用了几个右括号
        :param n: 要生产的括号对数
        :param result: 当前生成的结果
        :return:
        """
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n, result + '(')
        if right < left:
            self._gen(left, right + 1, n, result + ')')


if __name__ == '__main__':
    ret = Solution().generateParenthesis(3)
    assert len(ret) == 5
    ret = Solution().generateParenthesis2(3)
    assert len(ret) == 5
