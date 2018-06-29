package main

import (
	"fmt"
)

func isDividingNumber(num int) bool {
	n := num
	for n > 0 {
		digit := n % 10
		n = n / 10
		if digit != 0 && num%digit == 0 {
			continue
		} else {
			return false
		}
	}
	return true
}
func selfDividingNumbers(left int, right int) []int {
	result := []int{}
	for num := left; num <= right; num++ {
		if isDividingNumber(num) {
			result = append(result, num)
		}
	}
	return result
}

func main() {
	fmt.Println("[1,...,10,11,12,15,22]", selfDividingNumbers(1, 22))
}
