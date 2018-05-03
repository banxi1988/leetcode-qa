package main

import "fmt"

func findDisappearedNumbers(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		num := nums[i]
		numIndex := num - 1
		if num < 0 {
			numIndex = -num - 1
		}
		if nums[numIndex] > 0 {
			nums[numIndex] = -nums[numIndex]
		}
	}
	results := []int{}
	for i := 0; i < len(nums); i++ {
		if nums[i] > 0 {
			results = append(results, i+1)
		}
	}
	return results
}

func main() {
	fmt.Println("[5,6] -> ", findDisappearedNumbers([]int{4, 3, 2, 7, 8, 2, 3, 1}))
}
