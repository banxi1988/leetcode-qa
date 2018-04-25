package main

import "fmt"

func getSum(a, b int) int {
	sum := 0
	carry := 0
	for {
		sum = a ^ b
		carry = (a & b) << 1

		if carry == 0 {
			break
		}
		a = sum
		b = carry
	}
	return sum
}

func main() {
	fmt.Println(3 ^ 3)
	fmt.Println(1 << 3)
	fmt.Println("3 -> ", getSum(2, 1))
	fmt.Println("4 -> ", getSum(3, 1))
	fmt.Println("4 -> ", getSum(2, 2))
	fmt.Println("5 -> ", getSum(2, 3))
	fmt.Println("5 -> ", getSum(1, 4))
	fmt.Println("6 -> ", getSum(3, 3))
	fmt.Println("468 -> ", getSum(234, 234))
}
