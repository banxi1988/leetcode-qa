package main

import (
	"sort"
	"fmt"
)

func takenOne(coins []int, amount int) int {
	
}

func coinChange(coins []int, amount int) int {
	sort.Ints(coins)
}

func main() {
	fmt.Println("3 -> ", coinChange([]int{1, 2, 5}, 11))
	fmt.Println("-1 -> ", coinChange([]int{2}, 3))
}
