package main

import "fmt"

const (
	MaxInt = int(^uint(0) >> 1)
)

func minMoves(nums []int) int {
	numCount := len(nums)
	if numCount < 2 {
		return 0
	}
	//  M = otherSum - (n-1) *a
	minNum := MaxInt
	otherSum := 0
	for i := 0; i < numCount; i++ {
		num := nums[i]
		if num < minNum {
			minNum = num
		}
		otherSum += num
	}
	otherSum -= minNum
	m := otherSum - (numCount-1)*minNum

	return m
}

func main() {
	fmt.Println("0 ->", minMoves([]int{}))
	fmt.Println("0 ->", minMoves([]int{3}))
	fmt.Println("1 ->", minMoves([]int{2, 3}))
	fmt.Println("3 ->", minMoves([]int{1, 2, 3}))
	fmt.Println("5 ->", minMoves([]int{1, 3, 4}))
}
