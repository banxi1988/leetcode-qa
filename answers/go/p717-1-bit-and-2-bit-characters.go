package main

import (
	"fmt"
)

func isOneBitCharacter(bits []int) bool {
	bitCount := len(bits)
	if bitCount == 1 {
		return bits[0] == 0
	}
	if bitCount == 2 {
		return bits[0] == 0 && bits[1] == 0
	}

	if bits[0] == 0 {
		return isOneBitCharacter(bits[1:])
	} else {
		return isOneBitCharacter(bits[2:])
	}
}

func main() {
	fmt.Println("false -> ", isOneBitCharacter([]int{1, 0}))
	fmt.Println("true -> ", isOneBitCharacter([]int{0, 0}))
	fmt.Println("true -> ", isOneBitCharacter([]int{0}))
	fmt.Println("true -> ", isOneBitCharacter([]int{1, 1, 0}))
	fmt.Println("true -> ", isOneBitCharacter([]int{1, 0, 0}))
	fmt.Println("false -> ", isOneBitCharacter([]int{1, 1, 1, 0}))
	fmt.Println("false -> ", isOneBitCharacter([]int{1, 0, 1, 0}))
	fmt.Println("false -> ", isOneBitCharacter([]int{1, 0, 1, 0}))
}
