package main

import "fmt"
import "sort"

func missingNumber_v1(nums []int) int {
	sort.Ints(nums)
	for i := 0; i < len(nums); i++ {
		if i != nums[i] {
			return i
		}
	}
	return len(nums)
}

func missingNumber_v2(nums []int) int {
	n := len(nums)
	sumn := n * (n + 1) / 2
	sum := 0
	for i := 0; i < n; i++ {
		sum += nums[i]
	}
	return sumn - sum
}

func missingNumber(nums []int) int {
	num := 0
	for i := 0; i < len(nums); i++ {
		num ^= ((i + 1) ^ nums[i])
	}
	num ^= (len(nums) + 1)
	return num
}

func main() {
	fmt.Println("1 -> ", missingNumber([]int{0}))
	fmt.Println("2 -> ", missingNumber([]int{3, 0, 1}))
	fmt.Println("0 -> ", missingNumber([]int{3, 2, 1}))
	fmt.Println("3 -> ", missingNumber([]int{0, 2, 1}))
	fmt.Println("5 -> ", missingNumber([]int{6, 4, 3, 0, 2, 1}))
	fmt.Println("8 -> ", missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1}))
}
