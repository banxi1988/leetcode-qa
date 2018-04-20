package main

import "fmt"

func addDigits(num int) int {
	return (num-1)%9 + 1
}

func main() {
	fmt.Println("0 -> ", addDigits(0))
	fmt.Println("2 -> ", addDigits(38))
	fmt.Println("6 -> ", addDigits(96))
	fmt.Println("6 -> ", addDigits(222))
	fmt.Println("6 -> ", addDigits(123))
	fmt.Println("1 -> ", addDigits(19))
	fmt.Println(10 % 10)
}
