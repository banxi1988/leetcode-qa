package main

// 15 May 2018

import "fmt"

func nextGreaterElement(findNums []int, nums []int) []int {
	resultNums := make([]int, len(findNums))
	// num
	numsCount := len(nums)
	numIndexMap := make(map[int]int, numsCount)
	for i := 0; i < numsCount; i++ {
		numIndexMap[nums[i]] = i
	}
	for i := 0; i < len(findNums); i++ {
		target := findNums[i]
		result := -1
		j, _ := numIndexMap[target]
		for ; j < numsCount; j++ {
			if nums[j] > target {
				result = nums[j]
				break
			}
		}
		resultNums[i] = result
	}
	return resultNums
}

func main() {
	fmt.Println("[-1 3 -1] -> ", nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}))
	fmt.Println("[3,-1] -> ", nextGreaterElement([]int{2, 4}, []int{1, 2, 3, 4}))
}
