package main

import "fmt"

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	numCount := len(nums)
	if numCount < 2 {
		return false
	}
	for i := 0; i < numCount-1; i++ {
		numi := nums[i]
		for j := i + 1; j < numCount && j <= i+k; j++ {
			diff := numi - nums[j]
			if diff < 0 {
				diff = -diff
			}
			if diff <= t {
				return true
			}
		}
	}
	return false
}

func main() {
	fmt.Println("false > ", containsNearbyAlmostDuplicate([]int{1, 5, 2}, 1, 1))
	fmt.Println("true > ", containsNearbyAlmostDuplicate([]int{1, 2, 1}, 2, 1))
	fmt.Println("false > ", containsNearbyAlmostDuplicate([]int{1, 6, 12, 3}, 2, 2))
}
