package main

import "fmt"

func islandPerimeter(grid [][]int) int {
	rows := len(grid)
	if rows < 1 {
		return 0
	}
	cols := len(grid[0])

	calcCellPerimeter := func(row, col int) int {
		sides := 0
		// top
		if row == 0 || grid[row-1][col] == 0 {
			sides++
		}
		// right
		if col == (cols-1) || grid[row][col+1] == 0 {
			sides++
		}
		// bottom
		if row == (rows-1) || grid[row+1][col] == 0 {
			sides++
		}
		// left
		if col == 0 || grid[row][col-1] == 0 {
			sides++
		}
		return sides
	}

	perimeter := 0
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if grid[row][col] != 1 {
				continue
			}
			perimeter += calcCellPerimeter(row, col)
		}
	}
	return perimeter
}

func main() {
	grid1 := [][]int{
		{0, 1, 0, 0},
		{1, 1, 1, 0},
		{0, 1, 0, 0},
		{1, 1, 0, 0},
	}
	fmt.Println("16 -> ", islandPerimeter(grid1))
}
