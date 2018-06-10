package main

import (
	"fmt"
)

func rectangleArea(rectangles [][]int) int {
	area := 0
	for i := 0; i < len(rectangles); i++ {
		rect := rectangles[i]
	}
}

func main() {
	rects1 := [][]int{
		{0, 0, 2, 2},
		{1, 0, 2, 3},
		{1, 0, 3, 1},
	}
	fmt.Println("6 -> ", rectangleArea(rects1))
}
