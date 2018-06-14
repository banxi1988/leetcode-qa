package main

import (
	"fmt"
)

func findLengthOfLCIS(nums []int) int {
	if len(nums) < 1 {
		return 0
	}
	maxLen := 1
	curLen := 1
	prevNum := nums[0]
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		if num > prevNum {
			curLen++
		} else {
			if curLen > maxLen {
				maxLen = curLen
			}
			curLen = 1
		}
		prevNum = num
	}
	if curLen > maxLen {
		maxLen = curLen
	}
	return maxLen
}
func main() {
	fmt.Println("3 -> ", findLengthOfLCIS([]int{1, 3, 5, 4, 7}))
	fmt.Println("1 -> ", findLengthOfLCIS([]int{2, 2, 2, 2, 2}))
	fmt.Println("4 -> ", findLengthOfLCIS([]int{1, 3, 5, 4, 5, 6, 8}))
}
