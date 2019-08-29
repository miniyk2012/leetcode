from typing import List


def guess_password(table, length) -> List[str]:
    """假设有一个 4 位字母密码，每位密码是 a～e 之间的小写字母,
    编写一段代码，来暴力破解该密码"""

    def permutate(ele):
        if len(ele) == length:
            yield ele
            return
        for c in table:
            yield from permutate(ele + c)

    yield from permutate('')


if __name__ == "__main__":
    table = 'abcde'
    length = 4
    assert len(list(guess_password(table, length))) == len(table) ** length
