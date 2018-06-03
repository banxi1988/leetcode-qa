package main

import (
	"fmt"
	"sort"
)

func maximumProduct(nums []int) int {
	sort.Ints(nums)
	numCount := len(nums)
	min1 := nums[0]
	min2 := nums[1]

	max1 := nums[numCount-1]
	max2 := nums[numCount-2]
	max3 := nums[numCount-3]

	product1 := min1 * min2 * max1
	product2 := max1 * max2 * max3

	if product2 > product1 {
		return product2
	}
	return product1

}
func main() {
	fmt.Println("6 -> ", maximumProduct([]int{1, 2, 3}))
	fmt.Println("24 -> ", maximumProduct([]int{1, 2, 3, 4}))
	fmt.Println(3*6*4, " -> ", maximumProduct([]int{-3, -6, 3, 4}))
}
