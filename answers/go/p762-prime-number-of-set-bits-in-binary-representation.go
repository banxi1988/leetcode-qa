package main

import (
	"bytes"
	"fmt"
)

func countBit1(n int) int {
	num := n
	count := 0
	for num > 0 {
		if num&0x1 == 1 {
			count++
		}
		num = num >> 1
	}
	return count
}

func countPrimeSetBits(L int, R int) int {
	count := 0
	primes := []byte{
		2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
	}
	for num := L; num <= R; num++ {
		bit1Count := byte(countBit1(num))
		if bytes.IndexByte(primes, bit1Count) != -1 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println("3 -> ", countBit1(21))
	fmt.Println("4 -> ", countPrimeSetBits(6, 10))
	fmt.Println("5 -> ", countPrimeSetBits(10, 15))
}
