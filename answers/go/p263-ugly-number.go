package main

import "fmt"

func isUgly(num int) bool {
	if num == 0 {
		return false
	}
	for num%2 == 0 && num > 1 {
		num /= 2
	}
	for num%3 == 0 && num > 1 {
		num /= 3
	}
	for num%5 == 0 && num > 1 {
		num /= 5
	}
	if num == 1 {
		return true
	}
	return false
}

func main() {
	fmt.Println("false -> ", isUgly(0))
	fmt.Println("true -> ", isUgly(1))
	fmt.Println("true -> ", isUgly(6))
	fmt.Println("true -> ", isUgly(8))
	fmt.Println("false -> ", isUgly(14))
}
