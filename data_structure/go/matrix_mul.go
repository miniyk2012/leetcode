package main
import "fmt"

// 矩阵相乘
func matrixMul(a, b [][]int) [][]int {
    mat := [][]int{}
    for i := range a {
		mat = append(mat, []int{})
        for j := range b[0] {
            row := a[i]
            col := getCol(b, j)
			mat[i] = append(mat[i], vectorDot(row, col))
		}
	}
	return mat
}

func getCol(b [][]int, j int) []int {
    col := make([]int, len(b[0]))
    for i, row := range b {
		col[i] = row[j]
	}
    return col
}

func vectorDot(v1, v2 []int) int {
	sum := 0
	for i := range v1 {
		sum += v1[i] * v2[i]
	}
	return sum
}

func main() {
	mat := matrixMul(
		[][]int {
			{1, 2, 3},
			{3,4,5},
		},
		[][]int {
			{1,2,4},
            {3,4,5},
            {55,6,10},
		})
	fmt.Printf("%v", mat)
}