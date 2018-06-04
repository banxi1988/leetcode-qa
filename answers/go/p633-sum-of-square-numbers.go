package main

import (
	"fmt"
	"math"
)

func isPerfectSquare(num int) bool {
	// 平方数必定是3的倍数或者3的倍数+1。
	if !(num%3 == 0 || num%3 == 1) {
		return false
	}
	refRoot := math.Sqrt(float64(num))
	root := int(refRoot) - 2
	end := root + 3
	for root <= end {
		if root*root == num {
			return true
		}
		root++
	}
	return false
}

func judgeSquareSum(c int) bool {
	rootc := int(math.Sqrt(float64(c))) + 1
	for a := 0; a < rootc; a++ {
		powerB := c - a*a
		// 转为判断 powerB 是否可能为平方数
		if isPerfectSquare(powerB) {
			return true
		}

	}
	return false
}

func main() {
	// fmt.Println("false -> ", judgeSquareSum(3))
	fmt.Println("true -> ", judgeSquareSum(5))
	// fmt.Println("true -> ", judgeSquareSum(4))
	// fmt.Println("false -> ", judgeSquareSum(2147482647))
}
