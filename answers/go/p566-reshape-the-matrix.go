package main

import (
	"fmt"
)

func matrixReshape(nums [][]int, rows int, cols int) [][]int {
	numsRows := len(nums)
	numsCols := len(nums[0])
	numCount := numsRows * numsCols
	if numCount < rows*cols {
		return nums
	}
	result := [][]int{}
	for row := 0; row < rows; row++ {
		rowNums := make([]int, cols)
		for col := 0; col < cols; col++ {
			index := row*cols + col
			numRow := index / numsCols
			numCol := index % numsCols

			rowNums[col] = nums[numRow][numCol]
		}
		result = append(result, rowNums)
	}
	return result
}

func main() {
	arrA := [][]int{
		{1, 2},
		{3, 4},
	}
	arrB := [][]int{
		{1, 2},
		{3, 4},
	}
	fmt.Println("[1,2,3,4] -> ", matrixReshape(arrA, 1, 4))

	fmt.Println(arrB, " -> ", matrixReshape(arrB, 2, 4))
	arrC := [][]int{
		{1, 2, 3},
		{4, 5, 6},
	}
	fmt.Println("[[1 2] [3 4] [5 6]] -> ", matrixReshape(arrC, 3, 2))
}
