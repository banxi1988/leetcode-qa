package main

import "fmt"

func singleNumber(nums []int) int {
	numCountMap := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		count := numCountMap[num]
		numCountMap[num] = count + 1
	}
	for num, count := range numCountMap {
		if count == 1 {
			return num
		}
	}
	return 0
}

func main() {
	fmt.Println(" 5 -> ", singleNumber([]int{1, 3, 5, 3, 1}))
	fmt.Println(" 5 -> ", singleNumber([]int{1, 2, 1, 2, 5}))
	fmt.Println(" 1 -> ", singleNumber([]int{1, 2, 5, 2, 5}))
}
