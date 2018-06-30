package main

import (
	"fmt"
)

type MyPoint struct {
	Row int
	Col int
}

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	rowCount := len(image)
	colCount := len(image[0])
	sameColor := image[sr][sc]
	if sameColor == newColor {
		return image
	}
	points := []MyPoint{MyPoint{sr, sc}}
	visitPoint := func(row, col int) {
		if row < 0 || row >= rowCount || col < 0 || col >= colCount {
			return
		}
		if image[row][col] == sameColor {
			points = append(points, MyPoint{row, col})
		}
	}
	for len(points) > 0 {
		point := points[0]
		points = points[1:]
		row := point.Row
		col := point.Col
		image[row][col] = newColor
		// upper
		visitPoint(row-1, col)
		visitPoint(row+1, col)
		visitPoint(row, col-1)
		visitPoint(row, col+1)
	}
	return image
}

func main() {
	img1 := [][]int{
		{1, 1, 1},
		{1, 1, 0},
		{1, 0, 1},
	}
	fmt.Println("[[2,2,2],[2,2,0],[2,0,1]] -> ", floodFill(img1, 1, 1, 2))

	img2 := [][]int{
		{1, 1, 1, 1},
		{1, 1, 1, 0},
		{1, 0, 0, 1},
	}
	fmt.Println("[[2,2,2,2],[2,2,2,0],[2,0,0,1]] -> ", floodFill(img2, 1, 1, 2))
}
