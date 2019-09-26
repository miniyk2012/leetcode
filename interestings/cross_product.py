from typing import List, Any


def cross_product(matrix: List[List[Any]]) -> List[List[Any]]:

    def dfs(cur_ret: List[Any], idx: int) -> None:
        if idx == len(matrix):
            ret.append(cur_ret[:])
            return
        for ele in matrix[idx]:
            cur_ret.append(ele)
            dfs(cur_ret, idx+1)
            cur_ret.pop()

    ret = []
    dfs([], 0)
    return ret


def test_cross_product():
    matrix1 = [
        ['1', '2'],
        ['b'],
        ['A']
    ]
    assert len(cross_product(matrix1)) == 2

    matrix2 = [
        ['1', '3', '5'],
        ['b', 'd'],
        ['A', 'C']
    ]
    assert len(cross_product(matrix2)) == 12


if __name__ == "__main__":
    test_cross_product()
