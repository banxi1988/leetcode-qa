package main

import (
	"fmt"
	"math"
	"strconv"
)

func isPalindrome(num int) bool {
	if num < 10 {
		return true
	}
	numStr := strconv.Itoa(num)
	bytes := []byte(numStr)
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		if bytes[i] == bytes[j] {
			continue
		} else {
			return false
		}
	}
	return true
}

func isPrime(num int) bool {
	if num == 1 {
		return false
	}
	if num == 2 || num == 3 {
		return true
	}
	if num%6 != 1 && num%6 != 5 {
		return false
	}
	upper := int(math.Sqrt(float64(num))) + 1
	for i := 2; i <= upper; i++ {
		if num%i == 0 || num%(i+2) == 0 {
			return false
		}
	}
	return true

}

func primePalindrome(N int) int {
	num := N
	for {
		if isPalindrome(num) && isPrime(num) {
			return num
		}
		num++
	}
	return -1
}

func main() {
	fmt.Println("true ", isPalindrome(131))
	fmt.Println("true ", isPalindrome(11))
	fmt.Println("true ", isPalindrome(1))
	fmt.Println("false ", isPalindrome(132))
	fmt.Println("true ", isPrime(2))
	fmt.Println("true ", isPrime(3))
	fmt.Println("false ", isPrime(4))
	fmt.Println("true ", isPrime(5))

	fmt.Println("2 ->", primePalindrome(2))
	fmt.Println("7 ->", primePalindrome(6))
	fmt.Println("11 -> ", primePalindrome(8))
	fmt.Println("101 ->", primePalindrome(13))
	fmt.Println("1003001 ->", primePalindrome(995881))
	fmt.Println("100030001 ->", primePalindrome(9989900))

}
