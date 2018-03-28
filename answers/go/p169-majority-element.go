package main

import "fmt"

func majorityElement(nums []int) int {
	half := len(nums) / 2
	numCountMap := make(map[int]int)
	for _, num := range nums {
		count := numCountMap[num]
		if count >= half {
			return num
		}
		numCountMap[num] = count + 1
	}
	return 0
}

func main() {
	fmt.Println("3 -> ", majorityElement([]int{3, 2, 3}))
	fmt.Println("5 -> ", majorityElement([]int{5, 2, 5, 2, 5}))
}
