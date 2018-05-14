package main

// 14 May 2018

import (
	"fmt"
)

func constructRectangle(area int) []int {
	width := 1
	height := area
	minDiff := area
	diff := minDiff
	result := []int{height, width}

	rectArea := 0
	for width <= height {
		rectArea = width * height
		if rectArea == area {
			diff = height - width
			if diff < minDiff {
				minDiff = diff
				result[0] = height
				result[1] = width
			}
			width++
		} else if rectArea > area {
			height--
		} else {
			width++
		}
	}
	return result
}

func main() {
	fmt.Println("[1,1]-> ", constructRectangle(1))
	fmt.Println("[1,2]-> ", constructRectangle(2))
	fmt.Println("[1,3]-> ", constructRectangle(3))
	fmt.Println("[2,2]-> ", constructRectangle(4))
	fmt.Println("[1,5]-> ", constructRectangle(5))
	fmt.Println("[2,3]-> ", constructRectangle(6))
	fmt.Println("[2,4]-> ", constructRectangle(8))
	fmt.Println("[3,3]-> ", constructRectangle(9))
	fmt.Println("[2,5]-> ", constructRectangle(10))
	fmt.Println("[3,4]-> ", constructRectangle(12))
	fmt.Println("[2,7]-> ", constructRectangle(14))
	fmt.Println("[3,5]-> ", constructRectangle(15))
	fmt.Println("[3,6]-> ", constructRectangle(18))
	fmt.Println("[7,9]-> ", constructRectangle(63))
}
