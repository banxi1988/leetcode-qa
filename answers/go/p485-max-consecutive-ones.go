package main

import "fmt"

func findMaxConsecutiveOnes(nums []int) int {
	maxCount := 0
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			count++
		} else {
			if count > maxCount {
				maxCount = count
			}
			count = 0
		}
	}
	if count > maxCount {
		maxCount = count
	}
	return maxCount

}

func main() {
	fmt.Println("3 -> ", findMaxConsecutiveOnes([]int{1, 1, 0, 1, 1, 1}))
	fmt.Println("3 -> ", findMaxConsecutiveOnes([]int{1, 1, 1, 0, 1, 1}))
	fmt.Println("0 -> ", findMaxConsecutiveOnes([]int{0}))
	fmt.Println("1 -> ", findMaxConsecutiveOnes([]int{1}))
}
