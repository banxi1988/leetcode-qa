package leetcode

func areaOfXY(grid [][]int) int {
	area := 0
	for _, row := range grid {
		for _, p := range row {
			if p > 0 {
				area++
			}
		}
	}
	return area
}

func maxInts(nums []int) int {
	maxNum := -int(^uint(0)>>1) - 1
	for _, num := range nums {
		if num > maxNum {
			maxNum = num
		}
	}
	return maxNum
}

func areaOfYZ(grid [][]int) int {
	area := 0
	rowCount := len(grid)
	colCount := rowCount
	for col := 0; col < colCount; col++ {
		maxHeight := 0
		for row := 0; row < rowCount; row++ {
			if grid[row][col] > maxHeight {
				maxHeight = grid[row][col]
			}
		}
		area += maxHeight
	}
	return area
}

func areaOfZX(grid [][]int) int {
	area := 0
	for _, row := range grid {
		area += maxInts(row)
	}
	return area
}

func projectionArea(grid [][]int) int {
	return areaOfXY(grid) + areaOfYZ(grid) + areaOfZX(grid)
}
