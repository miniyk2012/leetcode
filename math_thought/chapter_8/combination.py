class Combination:

    def combine(self, table: str, m):
        """从table中抽m个元素的组合"""
        ret = []

        def _recusive(result, i):
            if len(result) == m:
                ret.append(result)
                return
            for idx, c in enumerate(table[i:], i):
                _recusive(result + c, idx+1)

        _recusive('', 0)
        return ret


if __name__ == '__main__':
    c = Combination()
    assert len(c.combine('1234', 4)) == 1
    print(c.combine('1234', 1))
    print(c.combine('1234', 2))
    print(c.combine('1234', 3))
