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
	log3 := math.Log10(float64(n)) / math.Log10(float64(3))
	log3if := float64(int(log3))
	epsilon := math.Nextafter(1.0, 2.0) - 1.0
	diff := log3 - log3if
	fmt.Println(n, log3, log3if, diff, epsilon)
	return diff <= epsilon*100
	// 3.0000000000000004 3   -4.440892098500626e-16
	// return log3 == log3if
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
	fmt.Println("true -> ", isPowerOfThree(4782969))
}
