package main

import (
	"fmt"
)

// func positionHash(row, col int) int {
// 	return row*100 + col
// }

func areaOfIsland(grid [][]int, row, col int) int {
	rowCount := len(grid)
	colCount := len(grid[0])
	if row < 0 || row >= rowCount || col < 0 || col >= colCount {
		return 0 // out of grid
	}
	if grid[row][col] == 1 {
		grid[row][col] = 0 // visited
		return 1 +
			areaOfIsland(grid, row+1, col) +
			areaOfIsland(grid, row-1, col) +
			areaOfIsland(grid, row, col+1) +
			areaOfIsland(grid, row, col-1)
	}
	return 0
}

func maxAreaOfIsland(grid [][]int) int {
	rowCount := len(grid)
	colCount := len(grid[0])

	maxArea := 0
	for row := 0; row < rowCount; row++ {
		for col := 0; col < colCount; col++ {
			if grid[row][col] == 0 {
				continue
			}
			area := areaOfIsland(grid, row, col)
			if area > maxArea {
				maxArea = area
			}
		}
	}
	return maxArea
}

func main() {
	grid := [][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}
	fmt.Println("6 -> ", maxAreaOfIsland(grid))
	grid1 := [][]int{
		{0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
		{0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0},
		{0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0},
		{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
	}
	fmt.Println("12 -> ", maxAreaOfIsland(grid1))

	grid2 := [][]int{
		{0, 0, 0, 0, 0, 0},
	}
	fmt.Println("0 -> ", maxAreaOfIsland(grid2))
}
