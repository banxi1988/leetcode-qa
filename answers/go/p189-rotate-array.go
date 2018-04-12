package main

import "fmt"

func rotate(nums []int, k int) {
	numCount := len(nums)
	if numCount < 2 {
		return
	}
	// reverse nums
	for i, j := 0, numCount-1; i < j; i, j = i+1, j-1 {
		tmp := nums[i]
		nums[i] = nums[j]
		nums[j] = tmp
	}

	divideIndex := k % numCount
	// reserve first k
	for i, j := 0, divideIndex-1; i < j; i, j = i+1, j-1 {
		tmp := nums[i]
		nums[i] = nums[j]
		nums[j] = tmp
	}

	// reserve after k
	for i, j := divideIndex, numCount-1; i < j; i, j = i+1, j-1 {
		tmp := nums[i]
		nums[i] = nums[j]
		nums[j] = tmp
	}
}

func main() {
	nums1 := []int{1, 2, 3, 4, 5, 6, 7}
	// [5,6,7,1,2,3,4]
	fmt.Println(nums1)
	rotate(nums1, 3)
	fmt.Println("expect [5,6,7,1,2,3,4] actual ", nums1)

	nums2 := []int{1, 2}
	rotate(nums2, 3)
	fmt.Println("expect [2,1] actual ", nums2)

	nums3 := []int{1, 2, 3}
	rotate(nums3, 4)
	fmt.Println("expect [3,1,2] actual ", nums3)
}
