package main

import (
	"fmt"
	"math"
)

func avg(nums []int) float64 {
	s := 0
	for _, num := range nums {
		s += num
	}
	return float64(s) / float64(len(nums))
}

func findMaxAverage(nums []int, k int) float64 {
	maxAvg := float64(math.MinInt32)
	for i := 0; i+k <= len(nums); i++ {
		curAvg := avg(nums[i : i+k])
		if curAvg > maxAvg {
			maxAvg = curAvg
		}
	}
	return maxAvg
}
func main() {
	fmt.Println("12.75 -> ", findMaxAverage([]int{1, 12, -5, -6, 50, 3}, 4))
	fmt.Println("-1.0 > ", findMaxAverage([]int{-1}, 1))
}
