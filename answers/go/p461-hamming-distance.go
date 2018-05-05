package main

import "fmt"

func hammingDistance(x, y int) int {
	count := 0
	for x > 0 || y > 0 {
		xbit := x & 0x1
		ybit := y & 0x1
		if xbit != ybit {
			count++
		}
		x = x >> 1
		y = y >> 1
	}
	return count
}

func main() {
	fmt.Println("2 -> ", hammingDistance(1, 4))
}
