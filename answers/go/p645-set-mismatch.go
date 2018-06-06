package main

import (
	"fmt"
)

func findErrorNums(nums []int) []int {
	numCount := len(nums)
	numMap := make(map[int]bool, numCount)
	dupNum := 0
	sum := 0
	for _, num := range nums {
		sum += num
		_, ok := numMap[num]
		if ok {
			dupNum = num
		} else {
			numMap[num] = true
		}
	}
	sum1n := numCount * (numCount + 1) / 2
	diff := sum1n - sum
	return []int{dupNum, dupNum + diff}

}
func main() {
	fmt.Println("[2,3]-> ", findErrorNums([]int{1, 2, 2, 4}))
	fmt.Println("[4,3]-> ", findErrorNums([]int{1, 2, 4, 4}))
	fmt.Println("[3,1]-> ", findErrorNums([]int{3, 2, 3, 4, 6, 5}))
}
