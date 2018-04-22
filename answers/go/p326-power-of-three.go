package main

import "fmt"
import "math"

func isPowerOfThree(n int) bool {
	if n == 0 {
		return false
	}
	if n == 1 {
		return true
	}
	if n%3 != 0 {
		return false
	}
	num := 3
	for num < n {
		num *= 3
	}
	return n == num

}

func main() {
	fmt.Println("false -> ", isPowerOfThree(0))
	fmt.Println("true -> ", isPowerOfThree(1))
	fmt.Println("true -> ", isPowerOfThree(3))
	fmt.Println("true -> ", isPowerOfThree(27))
	fmt.Println("false -> ", isPowerOfThree(2))
	fmt.Println("false -> ", isPowerOfThree(45))
	fmt.Println("true -> ", isPowerOfThree(81))
	fmt.Println("false -> ", isPowerOfThree(240))
	fmt.Println("true -> ", isPowerOfThree(243))
	fmt.Println(3^9, 3^27, 3^81, 3^243, math.Log(81))
}
