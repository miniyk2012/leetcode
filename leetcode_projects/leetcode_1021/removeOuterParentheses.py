class Solution:
    stack = []

    def removeOuterParentheses(self, S: str) -> str:
        parentheses_list = []
        current = ''
        for c in S:
            current += c
            if self.stack and self.stack[-1] == '(' and c == ')':
                self.stack.pop()
            else:
                self.stack.append(c)
            if not self.stack and current:
                parentheses_list.append(current[1:-1])
                current = ''

        return ''.join(parentheses_list)


if __name__ == '__main__':
    s = Solution()
    t = "(()())(())"
    ret = s.removeOuterParentheses(t)
    print(ret)

    t = "(()())(())(()(()))"
    ret = s.removeOuterParentheses(t)
    print(ret)
