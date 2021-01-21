class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_parentheses_positions = []
        right_redundant_positions = []
        for i, char in enumerate(s):
            if char == '(':
                left_parentheses_positions.append(i)
            if char == ')':
                if left_parentheses_positions:
                    left_parentheses_positions.pop()
                else:
                    right_redundant_positions.append(i)
        will_remove_positions = left_parentheses_positions + right_redundant_positions
        result = ''
        for i, char in enumerate(s):
            if i not in will_remove_positions:
                result += char
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.minRemoveToMakeValid('lee(t(c)o)de)')
    print(r)
    r = s.minRemoveToMakeValid("a)b(c)d")
    print(r)
    r = s.minRemoveToMakeValid("))((")
    print(r)
    r = s.minRemoveToMakeValid("(a(b(c)d)")
    print(r)
