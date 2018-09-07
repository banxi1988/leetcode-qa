package main

import (
	"fmt"
)

func peakIndexInMountainArray(nums []int) int {
	prevNum := nums[0]
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		if num < prevNum {
			return i - 1
		} else {
			prevNum = num
		}
	}
	return -1
}

func main() {
	fmt.Println("1 -> ", peakIndexInMountainArray([]int{0, 1, 0}))
	fmt.Println("1 -> ", peakIndexInMountainArray([]int{0, 2, 1, 0}))
	fmt.Println("2 -> ", peakIndexInMountainArray([]int{0, 2, 3, 2}))
}
