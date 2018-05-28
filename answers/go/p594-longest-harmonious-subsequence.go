package main

import (
	"fmt"
)

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func findLHS(nums []int) int {
	numCount := len(nums)
	if numCount < 2 {
		return numCount
	}
	start := 0
	maxLen := 0
	for start = 0; start < numCount-1; start++ {
		minNum := nums[start]
		maxNum := nums[start]
		end := start + 1
		for end < numCount {
			num := nums[end]
			if num < minNum {
				minNum = num
			}
			if num > maxNum {
				maxNum = num
			}
			if (maxNum - minNum) > 1 {
				break
			} else {
				end++
			}
		}
		curLen := end - start
		if curLen > maxLen {
			maxLen = curLen
		}
	}
	return maxLen
}
func main() {
	fmt.Println("1 -> ", findLHS([]int{1}))
	fmt.Println("1 -> ", findLHS([]int{1, 3}))
	fmt.Println("2 -> ", findLHS([]int{1, 2}))
	fmt.Println("2 -> ", findLHS([]int{1, 2, 3}))
	fmt.Println("3 -> ", findLHS([]int{2, 2, 3}))
	fmt.Println("5 -> ", findLHS([]int{1, 3, 2, 2, 2, 3, 7}))
}
