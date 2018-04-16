package main

import "fmt"

func containsNearbyDuplicate(nums []int, k int) bool {
	numCount := len(nums)
	if numCount < 2 {
		return false
	}
	for i := 0; i < numCount-1; i++ {
		numi := nums[i]
		for j := i + 1; j < numCount && j <= i+k; j++ {
			if numi == nums[j] {
				return true
			}
		}
	}
	return false
}

func main() {
	fmt.Println("false > ", containsNearbyDuplicate([]int{1, 2}, 2))
	fmt.Println("true > ", containsNearbyDuplicate([]int{1, 2, 1}, 2))
}
