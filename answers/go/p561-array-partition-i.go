package main

import (
	"fmt"
	"sort"
)

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums); i += 2 {
		sum += nums[i]
	}
	return sum
}

func main() {
	fmt.Println("4 -> ", arrayPairSum([]int{1, 2, 3, 4}))
	fmt.Println("9 -> ", arrayPairSum([]int{3, 5, 8, 6}))
}
