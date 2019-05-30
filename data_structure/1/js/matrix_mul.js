function matrixMul(a, b) {
    let mat = []

    for ( let i in a ) {
        let row = a[i] 
        mat.push([])
        for ( let j in b[0] ) {
            let num = vectorDot(row, getCol(b, j))
            mat[i].push(num)
        }
    }

    return mat
}

function vectorDot(v1, v2) {
    let sum = 0
    for ( let i in v1 )
        sum += v1[i] * v2[i]
    return sum
}

function getCol(b, j) {
    col = []
    for ( let i=0; i < b.length; i++ ) {
        col.push(b[i][j]);
    }
    return col;
}

mat = matrixMul(
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
console.log(mat)