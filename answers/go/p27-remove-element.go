package main

import "fmt"

func removeElement(nums []int, val int) int {
	newLen := 0

	for _, num := range nums {
		if num != val {
			nums[newLen] = num
			newLen++
		}
	}
	return newLen
}

func main() {
	arr1 := []int{1, 1, 2}
	fmt.Println(arr1, removeElement(arr1, 1), arr1)
	arr2 := []int{1, 1, 1, 2, 2, 3, 3, 4, 4}
	fmt.Println(arr2, removeElement(arr2, 2), arr2)

	arr3 := []int{1}
	fmt.Println(arr3, removeElement(arr3, 1), arr3)

	arr4 := []int{1, 2, 3, 4, 5}
	fmt.Println(arr4, removeElement(arr4, 5), arr4)
}
