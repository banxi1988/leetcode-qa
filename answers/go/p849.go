package main

import (
	"fmt"
)

func maxDistToClosest(seats []int) int {
	spaceStart := -1
	maxd := 1
	spaceCount := 0
	for i := 0; i < len(seats); i++ {
		seat := seats[i]
		if seat == 0 {
			if spaceStart < 0 {
				spaceStart = i
			}
			spaceCount++
		} else {
			if spaceCount > 1 {
				fmt.Println()
				if spaceStart == 0 {
					maxd = spaceCount
				} else {
					d := (spaceCount + 1) / 2
					if d > maxd {
						maxd = d
					}
				}
			}
			spaceCount = 0
			spaceStart = -1
		}
	}
	if spaceCount > 0 {
		if spaceCount > maxd {
			maxd = spaceCount
		}
	}
	return maxd
}

func main() {
	fmt.Println("2 -> ", maxDistToClosest([]int{1, 0, 0, 0, 1, 0, 1}))
	fmt.Println("3 -> ", maxDistToClosest([]int{1, 0, 0, 0}))
	fmt.Println("3 -> ", maxDistToClosest([]int{0, 0, 0, 1}))
	fmt.Println("1 -> ", maxDistToClosest([]int{1, 0, 0, 1}))
	fmt.Println("4 -> ", maxDistToClosest([]int{1, 1, 0, 0, 0, 0, 0, 0, 1}))
}
