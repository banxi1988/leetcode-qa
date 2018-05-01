package main

import "fmt"

func arrangeCoins(n int) int {
	rows := 0
	k := 1
	steps := n
	for steps >= k {
		steps -= k
		k++
		rows++
	}
	return rows
}

func main() {
	fmt.Println("1 -> ", arrangeCoins(1))
	fmt.Println("2 -> ", arrangeCoins(5))
	fmt.Println("3 -> ", arrangeCoins(8))
}
