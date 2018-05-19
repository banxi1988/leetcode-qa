package main

import (
	"fmt"
)

func checkPerfectNumber(num int) bool {
	for n := 2; n < 15; n++ {
		part1 := 1 << uint(n-1)
		part2 := (1 << uint(n)) - 1
		numn := part1 * part2
		if numn == num {
			return true
		} else if numn > num {
			return false
		}
	}
	return false
}

func main() {
	// 参考： https://zh.wikipedia.org/wiki/%E5%AE%8C%E5%85%A8%E6%95%B0
	fmt.Println("False -> ", checkPerfectNumber(1))
	fmt.Println("False -> ", checkPerfectNumber(2))
	fmt.Println("True -> ", checkPerfectNumber(6))
	fmt.Println("True -> ", checkPerfectNumber(28))
	fmt.Println("False -> ", checkPerfectNumber(18))
	fmt.Println("True -> ", checkPerfectNumber(496))
	fmt.Println("True -> ", checkPerfectNumber(8128))
	fmt.Println("False -> ", checkPerfectNumber(99999992))
}
