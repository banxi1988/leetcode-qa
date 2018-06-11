package main

import (
	"fmt"
)

func checkPossibility(nums []int) bool {
	prevNum := nums[0]
	changed := 0
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		if num < prevNum {
			// solution 1, lower prevNum
			changed++
			if changed > 1 {
				break
			}
			if i > 1 {
				prePrevNum := nums[i-2]
				if num < prePrevNum {
					changed++
					break
				}
			}
		}
		prevNum = num
	}
	if changed <= 1 {
		// fmt.Println(changed, " solution 1")
		return true
	}
	prevNum = nums[0]
	changed = 0
	for i := 1; i < len(nums); i++ {
		num := nums[i]
		if num < prevNum {
			// solution 2, inc currentNum
			changed++
			if changed > 1 {
				// fmt.Println("2 failed multiple times")
				break
			}

			if i < len(nums)-1 {
				nextNum := nums[i+1]
				if nextNum < prevNum {
					// fmt.Println("2 fail directly:", prevNum, nextNum)
					return false
				} else {
					num = nextNum
				}
			} else {
				// change lastOne
			}
		}
		prevNum = num
	}
	if changed <= 1 {
		// fmt.Println(changed, " solution 2")
	}
	return changed <= 1
}

func main() {
	fmt.Println("True -> ", checkPossibility([]int{4, 2}))
	fmt.Println("True -> ", checkPossibility([]int{4, 2, 3}))
	fmt.Println("True -> ", checkPossibility([]int{1, 2, 1}))
	fmt.Println("True -> ", checkPossibility([]int{3, 2, 5}))
	fmt.Println("True -> ", checkPossibility([]int{3, 2, 2}))
	fmt.Println("True -> ", checkPossibility([]int{2, 8, 3, 5}))
	fmt.Println("True -> ", checkPossibility([]int{2, 3, 3, 2, 4}))
	fmt.Println("False -> ", checkPossibility([]int{4, 2, 1}))
	fmt.Println("False -> ", checkPossibility([]int{4, 8, 3, 5}))
	fmt.Println("False -> ", checkPossibility([]int{2, 11, 9, 5}))
}
