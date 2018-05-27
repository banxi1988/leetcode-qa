package main

import (
	"fmt"
)

const (
	MAGIC_SUM = 15
)

func sumOfRow(row []int) int {
	sum := 0
	for _, num := range row {
		sum += num
	}
	return sum
}
func sumOfCol(square [][]int, col int) int {
	sum := 0
	for row := range square {
		sum += square[row][col]
	}
	return sum
}

func sumOfCross1(square [][]int) int {
	rows := len(square)
	cols := len(square[0])
	sum := 0
	for row, col := 0, 0; row < rows && col < cols; row, col = row+1, col+1 {
		sum += square[row][col]
	}
	return sum
}

func sumOfCross2(square [][]int) int {
	rows := len(square)
	cols := len(square[0])
	sum := 0
	for row, col := 0, cols-1; row < rows && col > -1; row, col = row+1, col-1 {
		sum += square[row][col]
	}
	return sum
}

func isMagicRow(row []int) bool {
	return sumOfRow(row) == MAGIC_SUM
}

func isMagicCol(square [][]int, col int) bool {
	return sumOfCol(square, col) == MAGIC_SUM
}

func isMagicCross(square [][]int) bool {
	return sumOfCross1(square) == MAGIC_SUM && sumOfCross2(square) == MAGIC_SUM
}

func isValidNums(square [][]int) bool {
	numMap := make(map[int]bool)
	N := len(square)
	for r := 0; r < N; r++ {
		for c := 0; c < N; c++ {
			num := square[r][c]
			if num < 1 || num > 9 {
				return false
			}
			_, ok := numMap[num]
			if ok {
				return false
			}
			numMap[num] = true
		}
	}
	return len(numMap) == 9
}

func isMagicSquare(square [][]int) bool {
	// check row sum
	for i := range square {
		fmt.Println("Row ", i)
		if !isMagicRow(square[i]) {
			// fmt.Println("Row sum failed: ", square)
			return false
		}
	}
	// check column
	for c := range square[0] {
		if !isMagicCol(square, c) {
			// fmt.Println("Col sum failed: ", square)
			return false
		}
	}
	// check cross
	ok := isMagicCross(square)
	if !ok {
		// fmt.Println("Cross sum failed: ", square)
		return false
	}

	ok = isValidNums(square)
	if !ok {
		// fmt.Println("Nums failed:", square)
	}
	return ok
}

func clipRect(grid [][]int, rowStart, colStart, size int) [][]int {
	rect := [][]int{}
	for r := 0; r < size; r++ {
		row := grid[rowStart+r][colStart : colStart+size]
		rect = append(rect, row)
	}
	return rect
}

func numMagicSquaresInside(grid [][]int) int {
	N := len(grid)
	D := 3
	count := 0
	for row := 0; row+D <= N; row++ {
		for col := 0; col+D <= N; col++ {
			square := clipRect(grid, row, col, D)
			if isMagicSquare(square) {
				// fmt.Println("MagicSquare:", square)
				count++
			}
		}
	}
	return count
}

func main() {
	arrA := [][]int{
		{4, 3, 8, 4},
		{9, 5, 1, 9},
		{2, 7, 6, 4},
	}
	fmt.Println("1 -> ", numMagicSquaresInside(arrA))

	arrB := [][]int{
		{1, 8, 6},
		{10, 5, 0},
		{4, 2, 9},
	}
	fmt.Println("0 -> ", numMagicSquaresInside(arrB))
}
