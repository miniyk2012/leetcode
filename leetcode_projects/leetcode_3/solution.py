class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest = 0
        while j<len(s):
            if s[j] in s[i:j]:
                if longest < j-i:
                    longest = j-i
                i = s.index(s[j], i) + 1
            else:
                j += 1
        if longest < j-i:
            longest = j-i
        return longest

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, max_length = 0, 0
        while start < len(s) and len(s) - start > max_length:
            end = start + 1
            while end < len(s):
                if s[end] in s[start:end]:
                    current_length = end - start
                    if current_length > max_length:
                        max_length = current_length
                    start += 1
                    break
                else:
                    end += 1
            else:
                current_length = end - start
                if current_length > max_length:
                    max_length = current_length
                start += 1
        return max_length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring2('abb'))
