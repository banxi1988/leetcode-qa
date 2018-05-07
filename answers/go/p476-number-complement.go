package main

import "fmt"

func findComplement(num int) int {
	com := 0
	base := 1 // 2^0
	for num > 0 {
		if 0x1&num == 0 {
			com += base
		}
		num = num >> 1
		base *= 2
	}
	return com
}

func main() {
	fmt.Println(" 2 -> ", findComplement(5))
	fmt.Println(" 0 -> ", findComplement(1))
}
