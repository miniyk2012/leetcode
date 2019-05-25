def matrix_mul(a, b):
    """
    矩阵相乘
    """
    mat = []
    for _ in range(len(a)):
        mat.append([0] * len(b[0]))

    for i in range(len(a)):
        for j in range(len(b[0])):
            row = a[i]
            col = get_col(b, j)
            mat[i][j] = vector_dot(row, col)
    return mat

def get_col(b, j):
    col = [0] * len(b)
    for i, row in enumerate(b):
        col[i] = row[j]
    return col

def vector_dot(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

if __name__ == "__main__":
    mat = matrix_mul(
        [
            [1,2,3],
            [3,4,5],
        ],
        [
            [1,2,4],
            [3,4,5],
            [55,6,10],
        ]
    )
    print(mat)