package main

import "fmt"

func isHappy(n int) bool {
	num := n
	for {
		sum := 0
		for num > 0 {
			digit := num % 10
			num = num / 10
			sum += digit * digit
		}
		if sum == 0 {
			return false
		}
		if sum == 1 {
			return true
		}
		if sum == n || sum == 4 {
			return false
		}
		num = sum
	}
	return false
}

func main() {
	fmt.Println("false ->", isHappy(0))
	fmt.Println("true ->", isHappy(100))
	fmt.Println("true ->", isHappy(1))
	fmt.Println("false ->", isHappy(2))
	fmt.Println("true ->", isHappy(7))
	fmt.Println("true ->", isHappy(10))
	fmt.Println("true ->", isHappy(13))
	fmt.Println("true ->", isHappy(19))
	fmt.Println("true ->", isHappy(28))
	fmt.Println("true ->", isHappy(31))
	fmt.Println("true ->", isHappy(32))
	fmt.Println("false ->", isHappy(37))
	fmt.Println("false ->", isHappy(18))
}
