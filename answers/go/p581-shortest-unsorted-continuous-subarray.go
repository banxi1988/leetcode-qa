package main

import (
	"fmt"
	"sort"
)

func findUnsortedSubarray(nums []int) int {
	sortedNums := make([]int, len(nums))
	copy(sortedNums, nums)
	sort.Ints(sortedNums)
	start := 0
	for start < len(nums) {
		if sortedNums[start] == nums[start] {
			start++
		} else {
			break
		}
	}

	end := len(nums) - 1
	for end > start {
		if sortedNums[end] == nums[end] {
			end--
		} else {
			break
		}
	}
	rangeLen := end - start + 1
	// fmt.Println("Local:", start, " - ", end, "  ===> ", rangeLen)
	return rangeLen
}

func main() {
	fmt.Println("0 -> ", findUnsortedSubarray([]int{2}))
	fmt.Println("0 -> ", findUnsortedSubarray([]int{2, 3}))
	fmt.Println("0 -> ", findUnsortedSubarray([]int{2, 3, 4}))
	fmt.Println("2 -> ", findUnsortedSubarray([]int{3, 2}))
	fmt.Println("3 -> ", findUnsortedSubarray([]int{1, 4, 2, 3}))
	fmt.Println("3 -> ", findUnsortedSubarray([]int{1, 4, 2, 3, 6}))
	fmt.Println("5 -> ", findUnsortedSubarray([]int{2, 6, 4, 8, 10, 9, 15}))
}
