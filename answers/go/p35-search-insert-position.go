package main

import "fmt"

func searchInsert(nums []int, target int) int {
	low := 0
	high := len(nums)
	for low < high {
		index := (low + high) / 2
		num := nums[index]
		if target > num {
			low = index + 1
		} else {
			high = index
		}

	}
	return low
}

func main() {
	arr1 := []int{1, 3, 5, 6}
	fmt.Println(arr1, 2, searchInsert(arr1, 5))
	fmt.Println(arr1, 1, searchInsert(arr1, 2))
	fmt.Println(arr1, 2, searchInsert(arr1, 4))
	fmt.Println(arr1, 0, searchInsert(arr1, 0))
	fmt.Println(arr1, 4, searchInsert(arr1, 7))

	arr2 := []int{1}
	fmt.Println(arr2, 0, searchInsert(arr2, 0))
	fmt.Println(arr2, 1, searchInsert(arr2, 2))

	arr3 := []int{1, 3, 5}
	fmt.Println(arr3, 2, searchInsert(arr3, 5))
	fmt.Println(arr3, 1, searchInsert(arr3, 2))
	fmt.Println(arr3, 2, searchInsert(arr3, 4))
	fmt.Println(arr3, 0, searchInsert(arr3, 0))
	fmt.Println(arr3, 3, searchInsert(arr3, 7))
}
