package main

import (
	"fmt"
)

func isToeplitzMatrix(matrix [][]int) bool {
	maxColumn := len(matrix[0])
	maxRow := len(matrix)

	for i := 0; i < maxColumn; i++ {
		prevNum := matrix[0][i]
		for k := 1; k < maxRow && k+i < maxColumn; k++ {
			// fmt.Println(k, k+i)
			if matrix[k][i+k] == prevNum {
				continue
			} else {
				return false
			}
		}
	}
	for r := 1; r < maxRow; r++ {
		prevNum := matrix[r][0]
		for k := 1; k < maxColumn && r+k < maxRow; k++ {
			if matrix[r+k][k] == prevNum {
				continue
			} else {
				return false
			}
		}
	}
	return true
}

func main() {
	matrix1 := [][]int{
		{1, 2, 3, 4},
		{5, 1, 2, 3},
		{9, 5, 1, 2},
	}

	matrix2 := [][]int{
		{1, 2},
		{2, 2},
	}
	matrix3 := [][]int{
		{1, 2, 3, 4, 6},
		{5, 1, 2, 3, 4},
		{9, 5, 1, 2, 3},
		{9, 9, 5, 1, 2},
	}
	matrix4 := [][]int{
		{1, 2, 3, 4, 6},
		{5, 1, 2, 3, 4},
		{9, 5, 1, 2, 3},
		{9, 6, 5, 1, 2},
	}
	matrix5 := [][]int{
		{1, 2, 3, 4, 6},
		{5, 1, 2, 3, 5},
		{9, 5, 1, 2, 3},
		{9, 9, 5, 1, 2},
	}
	fmt.Println("True -> ", isToeplitzMatrix(matrix1))
	fmt.Println("False -> ", isToeplitzMatrix(matrix2))
	fmt.Println("True -> ", isToeplitzMatrix(matrix3))
	fmt.Println("False -> ", isToeplitzMatrix(matrix4))
	fmt.Println("False -> ", isToeplitzMatrix(matrix5))
}
