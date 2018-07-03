package main

import (
	"fmt"
)

func dominantIndex(nums []int) int {
	maxNum := -1
	maxIndex := 0
	for index, num := range nums {
		if num > maxNum {
			maxNum = num
			maxIndex = index
		}
	}
	for index, num := range nums {
		if index == maxIndex {
			continue
		}
		if num*2 <= maxNum {
			continue
		} else {
			return -1
		}
	}
	return maxIndex
}

func main() {
	fmt.Println("1 -> ", dominantIndex([]int{3, 6, 1, 0}))
	fmt.Println("-1 -> ", dominantIndex([]int{1, 2, 3, 4}))
	fmt.Println("0 -> ", dominantIndex([]int{3}))
}
