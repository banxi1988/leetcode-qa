package main

import (
	"fmt"
)

func incLen(nums []int) int {
	numCount := len(nums)
	if numCount < 2 {
		return numCount
	}
	prev := nums[0]
	length := 1
	for i := 1; i < numCount; i++ {
		if nums[i] > prev {
			prev = nums[i]
			length++
		} else {
			break
		}
	}
	return length
}

func decLen(nums []int) int {
	numCount := len(nums)
	if numCount < 2 {
		return numCount
	}
	prev := nums[0]
	length := 1
	for i := 1; i < numCount; i++ {
		if nums[i] < prev {
			prev = nums[i]
			length++
		} else {
			break
		}
	}
	return length
}

func longestMountain(A []int) int {
	maxLen := 0
	for i := 0; i < (len(A) - 2); i++ {
		arr := A[i:]
		iLen := incLen(arr)
		if iLen < 2 {
			continue
		}
		dLen := decLen(arr[iLen-1:])
		if dLen < 2 {
			continue
		}
		curLen := iLen + dLen - 1
		if curLen > maxLen {
			maxLen = curLen
		}
	}
	return maxLen
}

func main() {
	fmt.Println("0 -> ", longestMountain([]int{1, 1, 0, 1}))
	fmt.Println("0 -> ", longestMountain([]int{1, 1, 1}))
	fmt.Println("0 -> ", longestMountain([]int{1, 2, 2}))
	fmt.Println("3 -> ", longestMountain([]int{1, 2, 1}))
	fmt.Println("5 -> ", longestMountain([]int{2, 1, 4, 7, 3, 2, 5}))
}
