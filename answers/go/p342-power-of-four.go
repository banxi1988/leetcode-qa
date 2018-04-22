package main

import "fmt"
import "math"

func isPowerOfFour(n int) bool {
	if n <= 0 {
		return false
	}
	if n == 1 {
		return true
	}
	if n%4 != 0 {
		return false
	}
	log4 := math.Log10(float64(n)) / math.Log10(float64(4))
	log4if := math.Round(log4)
	if log4 == log4if {
		return true
	}
	epsilon := math.Nextafter(1.0, 2.0) - 1.0
	diff := math.Abs(log4 - log4if)
	fmt.Println(n, log4, log4if, diff, epsilon)
	return diff <= epsilon*10
}

func main() {
	fmt.Println("false -> ", isPowerOfFour(0))
	fmt.Println("true -> ", isPowerOfFour(1))
	fmt.Println("true -> ", isPowerOfFour(4))
	fmt.Println("true -> ", isPowerOfFour(16))
	fmt.Println("false -> ", isPowerOfFour(2))
	fmt.Println("false -> ", isPowerOfFour(45))
	fmt.Println("true -> ", isPowerOfFour(64))
	fmt.Println("false -> ", isPowerOfFour(240))
	fmt.Println("true -> ", isPowerOfFour(1024))
	fmt.Println("true -> ", isPowerOfFour(262144))
	fmt.Println("true -> ", isPowerOfFour(4194304))
}
