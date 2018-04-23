package main

import "fmt"

func isPerfectSquare(num int) bool {
	if num == 1 || num == 4 {
		return true
	}
	root := 1
	end := num / 2
	for root < end {
		if root*root == num {
			return true
		}
		root++
	}
	return false
}

func main() {
	fmt.Println("true -> ", isPerfectSquare(4))
	fmt.Println("true -> ", isPerfectSquare(9))
	fmt.Println("false -> ", isPerfectSquare(8))
	fmt.Println("true -> ", isPerfectSquare(16))
	fmt.Println("false -> ", isPerfectSquare(14))
}
