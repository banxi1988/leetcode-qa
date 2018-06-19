package main

import (
	"fmt"
)

func hasAlternatingBits(n int) bool {
	bits := n
	prevBit := bits & 0x1
	bits = bits >> 1
	for bits > 0 {
		// fmt.Println("Bits ", bits)
		curBit := bits & 0x1
		if prevBit == curBit {
			return false
		}
		prevBit = curBit
		bits = bits >> 1
	}
	return true
}

func main() {
	fmt.Println("true -> ", hasAlternatingBits(1))
	fmt.Println("true -> ", hasAlternatingBits(2))
	fmt.Println("false -> ", hasAlternatingBits(3))
	fmt.Println("false -> ", hasAlternatingBits(4))
	fmt.Println("true -> ", hasAlternatingBits(5))
	fmt.Println("false -> ", hasAlternatingBits(6))
	fmt.Println("true -> ", hasAlternatingBits(10))
	fmt.Println("false -> ", hasAlternatingBits(11))
}
