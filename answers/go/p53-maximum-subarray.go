package main

import "fmt"

func maxSubArray(nums []int) int {
	maxSum := nums[0]
	sum := maxSum
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		if sum < 0 {
			sum = num
		} else {
			sum += num
		}
		if sum > maxSum {
			maxSum = sum
		}
	}
	return maxSum
}

func main() {
	arr1 := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}
	fmt.Println("expect=6,actual=", maxSubArray(arr1))

	arr2 := []int{-2, 1, -3, 4, -1, 2, 1, -5, 4, -8, 9}
	fmt.Println("expect=9,actual=", maxSubArray(arr2))

	arr3 := []int{-2}
	fmt.Println("expect=-2,actual=", maxSubArray(arr3))
}
