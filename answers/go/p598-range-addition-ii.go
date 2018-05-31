package main

import (
	"fmt"
)

func maxCount(m int, n int, ops [][]int) int {
	minCols := n
	minRows := m
	for _, op := range ops {
		row := op[0]
		col := op[1]
		if row < minRows {
			minRows = row
		}
		if col < minCols {
			minCols = col
		}
	}
	return minRows * minCols
}

func main() {
	fmt.Println("4 -> ", maxCount(3, 3, [][]int{
		{2, 2},
		{3, 3},
	}))
	fmt.Println("1600000000 -> ", maxCount(40000, 40000, [][]int{}))
}
