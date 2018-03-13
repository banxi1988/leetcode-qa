package main

import "fmt"

func removeDuplicates(nums []int) int {
	numCount := len(nums)
	if numCount < 2{
		return numCount
	}
   prevNum := nums[0] 
   newLen := 1
   for _, num := range nums[1:]{
		if num != prevNum{
			prevNum = num
			nums[newLen] = num
			newLen++
		}
   } 
   return newLen
}

func main(){
	arr1 := []int{1,1,2}
	fmt.Println(arr1, removeDuplicates(arr1), arr1)
	arr2 := []int{1,1,1,2,2,3,3,4,4}
	fmt.Println(arr2, removeDuplicates(arr2), arr2)

	arr3 := []int{1}
	fmt.Println(arr3, removeDuplicates(arr3), arr3)

	arr4 := []int{1,2,3,4,5}
	fmt.Println(arr4, removeDuplicates(arr4), arr4)
}