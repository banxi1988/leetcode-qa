package main

import (
	"fmt"
)

func mini(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func distributeCandies(candies []int) int {
	kindMap := make(map[int]int)
	for _, k := range candies {
		count, _ := kindMap[k]
		kindMap[k] = count + 1
	}
	return mini(len(candies)/2, len(kindMap))

}
func main() {
	fmt.Println("3 -> ", distributeCandies([]int{1, 1, 2, 2, 3, 3}))
	fmt.Println("2 -> ", distributeCandies([]int{1, 1, 2, 3}))
	fmt.Println("3 -> ", distributeCandies([]int{1, 1, 1, 1, 2, 2, 2, 3, 3, 3}))
}
