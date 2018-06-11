package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func calcNewPixel(M [][]int, row int, col int) int {
	rows := len(M)
	cols := len(M[0])
	rowStart := max(0, row-1)
	rowEnd := min(rows-1, row+1)
	colStart := max(0, col-1)
	colEnd := min(cols-1, col+1)

	sum := 0
	count := 0
	for row := rowStart; row <= rowEnd; row++ {
		rowNums := M[row]
		for col := colStart; col <= colEnd; col++ {
			sum += rowNums[col]
			count++
		}
	}
	return sum / count
}

func imageSmoother(M [][]int) [][]int {
	rows := len(M)
	cols := len(M[0])
	newImage := make([][]int, rows)
	for row := 0; row < rows; row++ {
		rowPixels := make([]int, cols)
		for col := 0; col < cols; col++ {
			rowPixels[col] = calcNewPixel(M, row, col)
		}
		newImage[row] = rowPixels
	}
	return newImage
}

func main() {
	arrA := [][]int{
		{1, 1, 1},
		{1, 0, 1},
		{1, 1, 1},
	}
	expected := [][]int{
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0},
	}
	fmt.Println(expected, " -> ", imageSmoother(arrA))

	imgB := [][]int{
		{2, 3, 4}, {5, 6, 7}, {8, 9, 10}, {11, 12, 13}, {14, 15, 16},
	}
	fmt.Println("[[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]")
	fmt.Println(" -> ", imageSmoother(imgB))
}
