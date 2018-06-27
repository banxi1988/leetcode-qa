package main

import (
	"fmt"
)

func sum(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	return s
}

func pivotIndex(nums []int) int {
	numCount := len(nums)
	if numCount < 1 {
		return -1
	}
	if numCount == 1 {
		return 0
	}
	leftSum := 0
	rightSum := sum(nums[1:])
	for index := 0; index < numCount; index++ {
		if leftSum == rightSum {
			return index
		}
		leftSum += nums[index]
		if index+1 < numCount {
			rightSum -= nums[index+1]
		}
	}
	return -1
}

func main() {
	fmt.Println("3 -> ", pivotIndex([]int{1, 7, 3, 6, 5, 6}))
	fmt.Println("-1 -> ", pivotIndex([]int{1, 2, 3}))
	fmt.Println("1 -> ", pivotIndex([]int{1, 2, 1}))
	fmt.Println("1 -> ", pivotIndex([]int{1, 2, 2, -1}))
	fmt.Println("4 -> ", pivotIndex([]int{1, 1, 2, 2, 2, 6}))
	fmt.Println("1 -> ", pivotIndex([]int{6, 2, 1, 5}))
	fmt.Println("0 -> ", pivotIndex([]int{-1, -1, -1, 0, 1, 1}))
	fmt.Println("5 -> ", pivotIndex([]int{-1, -1, 0, 1, 1, 0}))
}
