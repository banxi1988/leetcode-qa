package main

import "fmt"

import "math"

func reverse(x int) int {
	sign := 1
	num := x
	if x < 0 {
		sign = -1
		num = -x
	}
	result := 0
	for num > 0 {
		result *= 10
		result += num % 10
		num /= 10
	}
	result = result * sign
	if result > math.MaxInt32 {
		return 0
	} else if result < math.MinInt32 {
		return 0
	}
	return result
}

func main() {
	fmt.Println("123 ->(321) ", reverse(123))
	fmt.Println("-123 ->(-321) ", reverse(-123))
	fmt.Println("120 ->(21) ", reverse(120))
	fmt.Println("2147483647 ->(0) ", reverse(2147483647))
}
