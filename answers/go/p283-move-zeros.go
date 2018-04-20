package main

import "fmt"

func moveZeroes(nums []int) {
	numCount := len(nums)

	for i := 0; i < numCount-1; i++ {
		num := nums[i]
		if num != 0 {
			continue
		}
		for j := i + 1; j < numCount; j++ {
			numj := nums[j]
			if numj != 0 {
				nums[i] = numj
				nums[j] = 0
				break
			}
		}
		// fmt.Println(nums)
	}
}

func main() {
	nums1 := []int{0, 1, 0, 3, 12}
	moveZeroes(nums1)
	fmt.Println(nums1)

	nums2 := []int{7, 0, 1, 0, 3, 0, 12}
	moveZeroes(nums2)
	fmt.Println(nums2)

	nums3 := []int{0, 0}
	moveZeroes(nums3)
	fmt.Println(nums3)

	nums4 := []int{1}
	moveZeroes(nums4)
	fmt.Println(nums4)
}
