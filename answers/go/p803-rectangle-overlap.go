package main

import (
	"fmt"
)

func isRectangleOverlap(rect1 []int, rect2 []int) bool {
	left1 := rect1[0]
	bottom1 := rect1[1]
	right1 := rect1[2]
	top1 := rect1[3]
	left2 := rect2[0]
	bottom2 := rect2[1]
	right2 := rect2[2]
	top2 := rect2[3]
	// take rect1 as center,judge where rect2
	// rect2 is in right side
	if right2 > left1 && left2 < right1 {
		return bottom2 < top1 && top2 > bottom1
	}

	return false
}
func main() {
	fmt.Println("true -> ", isRectangleOverlap([]int{0, 0, 2, 2}, []int{1, 1, 3, 3}))
	fmt.Println("false -> ", isRectangleOverlap([]int{0, 0, 1, 1}, []int{1, 0, 2, 1}))
}
