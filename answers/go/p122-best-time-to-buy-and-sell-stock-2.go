package main

import "fmt"

func maxProfit(prices []int) int {
	max := 0
	daysCount := len(prices)
	for sellIndex := 1; sellIndex < daysCount; sellIndex++ {
		profit := prices[sellIndex] - prices[sellIndex-1]
		if profit > 0 {
			max += profit
		}
	}
	return max
}

func main() {
	fmt.Println(" 7 -> ", maxProfit([]int{7, 1, 5, 3, 6, 4}))
	fmt.Println(" 0 -> ", maxProfit([]int{7, 6, 4, 3, 1}))
	fmt.Println(" 5 -> ", maxProfit([]int{7, 1, 2, 5, 6, 4}))
}
