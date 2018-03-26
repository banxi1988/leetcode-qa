package main

import "fmt"

func maxProfit(prices []int) int {
	max := 0
	daysCount := len(prices)
	for buyIndex := 0; buyIndex < (daysCount - 1); buyIndex++ {
		for sellIndex := buyIndex + 1; sellIndex < daysCount; sellIndex++ {
			profit := prices[sellIndex] - prices[buyIndex]
			if profit > max {
				max = profit
			}
		}
	}
	return max
}

func main() {
	fmt.Println(" 5 -> ", maxProfit([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(" 0 -> ", maxProfit([]int{7, 6, 4, 3, 1}))
}
