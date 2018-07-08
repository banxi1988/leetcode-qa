package main

import (
	"fmt"
)

func transpose(A [][]int) [][]int {
	rowCount := len(A)
	colCount := len(A[0])

	result := make([][]int, colCount)
	for col := 0; col < colCount; col++ {
		rowNums := make([]int, rowCount)
		for row := 0; row < rowCount; row++ {
			rowNums[row] = A[row][col]
		}
		result[col] = rowNums
	}
	return result
}

func main() {
	arrA := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}
	fmt.Println("[1,4,7][2,5,8][3,6,9] -> ", transpose(arrA))
	arrB := [][]int{
		{1, 2, 3},
		{4, 5, 6},
	}
	fmt.Println("[1,4][2,5][3,6] -> ", transpose(arrB))
}
