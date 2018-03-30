package main

import "fmt"

func trailingZeroes(n int) int {
	fiveFactors := 0
	baseNum := 5
	for baseNum <= n {
		fiveFactors += n / baseNum
		baseNum *= 5
	}
	return fiveFactors
}

func main() {
	// 阶乘计算可以参考 http://www.wolframalpha.com/input/?i=25!
	fmt.Println("0 -> ", trailingZeroes(0))
	fmt.Println("0 -> ", trailingZeroes(1))
	fmt.Println("0 -> ", trailingZeroes(2))
	fmt.Println("1 -> ", trailingZeroes(5))
	fmt.Println("1 -> ", trailingZeroes(6))
	fmt.Println("2 -> ", trailingZeroes(10))
	fmt.Println("3 -> ", trailingZeroes(15))
	fmt.Println("4 -> ", trailingZeroes(20))
	fmt.Println("6 -> ", trailingZeroes(25))
	fmt.Println("7 -> ", trailingZeroes(30))
	fmt.Println("9 -> ", trailingZeroes(40))
	fmt.Println("49 -> ", trailingZeroes(200))
	fmt.Println("62 -> ", trailingZeroes(250))
	fmt.Println("156 -> ", trailingZeroes(625))
	fmt.Println("452137076 -> ", trailingZeroes(1808548329))
}
