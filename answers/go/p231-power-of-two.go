package main

import "fmt"

func isPowerOfTwo(n int) bool {
	if n < 1 {
		return false
	}
	num := n
	for num > 1 {
		r := num % 2
		if r != 0 {
			return false
		}
		num = num / 2
	}
	return true
}

func main() {
	fmt.Println("false -> ", isPowerOfTwo(0))
	fmt.Println("true -> ", isPowerOfTwo(1))
	fmt.Println("true -> ", isPowerOfTwo(2))
	fmt.Println("false -> ", isPowerOfTwo(3))
	fmt.Println("true -> ", isPowerOfTwo(4))
	fmt.Println("false -> ", isPowerOfTwo(5))
	fmt.Println("false -> ", isPowerOfTwo(6))
	fmt.Println("false -> ", isPowerOfTwo(7))
	fmt.Println("true -> ", isPowerOfTwo(8))
	fmt.Println("false -> ", isPowerOfTwo(-16))
}
