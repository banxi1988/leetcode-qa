package main

import "fmt"

func containsDuplicate(nums []int) bool {
	numMap := make(map[int]bool)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		_, hasDuplicate := numMap[num]
		if hasDuplicate {
			return true
		}
		numMap[num] = true
	}
	return false
}

func main() {
	fmt.Println(" true > ", containsDuplicate([]int{1, 2, 1}))
	fmt.Println(" true > ", containsDuplicate([]int{1, 2, 2}))
	fmt.Println(" true > ", containsDuplicate([]int{2, 2}))
	fmt.Println(" false > ", containsDuplicate([]int{1, 2}))
	fmt.Println(" false > ", containsDuplicate([]int{1}))
	fmt.Println(" false > ", containsDuplicate([]int{1, 2, 3}))
}
