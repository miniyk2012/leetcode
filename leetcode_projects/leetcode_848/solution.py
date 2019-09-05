from typing import List


class Solution:
    LETTER_SIZE = 26

    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ret = ''
        pre = 0
        length = len(S)
        ord_a = ord('a')
        for idx, shift in enumerate(shifts[::-1]):
            word_idx = length - idx - 1
            shift += pre
            # shift %= self.LETTER_SIZE  # python不怕整数溢出, 注释掉略微提速
            pre = shift
            code = ord_a + (ord(S[word_idx]) - ord_a + shift) % self.LETTER_SIZE
            ret = chr(code) + ret
        return ret


def test():
    s = Solution()
    ret = s.shiftingLetters("abc", [3, 5, 9])
    assert ret == "rpl"


if __name__ == '__main__':
    test()
