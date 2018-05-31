package main

import (
	"fmt"
)

func canPlaceFlowers(flowerbed []int, n int) bool {
	seedCount := 0
	spaceCount := 1 // we can place at the start
	for i := 0; i < len(flowerbed); i++ {
		if flowerbed[i] == 0 {
			if spaceCount == 2 {
				// now we can place at i - 1 or i (if i == 0)
				seedCount++
				// reset spaceCount
				spaceCount = 1
			} else {
				spaceCount++
			}
		} else {
			spaceCount = 0
		}
	}
	if spaceCount == 2 {
		seedCount++ // we can place at the end
	}
	return seedCount >= n
}

func main() {
	fmt.Println("True -> ", canPlaceFlowers([]int{1, 0, 0, 0, 1}, 1))
	fmt.Println("True -> ", canPlaceFlowers([]int{1, 0, 0, 0, 0}, 2))
	fmt.Println("False -> ", canPlaceFlowers([]int{1, 0, 0, 0, 1}, 2))
	fmt.Println("False -> ", canPlaceFlowers([]int{0, 1, 0}, 1))
	fmt.Println("True -> ", canPlaceFlowers([]int{0, 0, 1, 0, 0}, 1))
	fmt.Println("True -> ", canPlaceFlowers([]int{0, 0, 1, 0, 0}, 2))
}
