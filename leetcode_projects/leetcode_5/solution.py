class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        length = len(s)
        current_longest = ''
        for i in range(0, length):
            for j in range(length-1, i-1, -1):
                if j - i + 1 <= longest:
                    break
                remain = s[i:j + 1]
                if self.judge_Palindrome(remain):
                    longest = j - i + 1
                    current_longest = remain
        return current_longest

    def judge_Palindrome(self, remain):
        reversed_remain = remain[::-1]
        return remain == reversed_remain


if __name__ == '__main__':
    solution = Solution()
    datas = ["abacab"]
    for data in datas:
        result = solution.longestPalindrome(data)
        print(result)
