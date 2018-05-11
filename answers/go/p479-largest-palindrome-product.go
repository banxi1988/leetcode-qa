package main

import "fmt"
import "strconv"
import "math"

func makePalindrome(num int) int {
	numStr := strconv.Itoa(num)
	numBytes := []byte(numStr)
	palindrome := []byte(numStr)
	digitsCount := len(numBytes)
	for i := digitsCount - 1; i > -1; i-- {
		palindrome = append(palindrome, numBytes[i])
	}
	palindromNumStr := string(palindrome)
	palindromeNum, _ := strconv.Atoi(palindromNumStr)
	return palindromeNum
}

func largestPalindrome(n int) int {
	if n == 1 {
		return 9
	}
	upbound := int(math.Pow10(n)) - 1
	downbound := upbound / 10
	for i := upbound; i > downbound; i-- {
		palindrome := makePalindrome(i)
		for j := upbound; j > downbound && palindrome < j*j; j-- {
			if palindrome%j == 0 {
				//fmt.Println(palindrome, j)
				return palindrome % 1337
			}
		}
	}
	return 0
}

func main() {
	fmt.Println(makePalindrome(98))
	fmt.Println(" 9 -> ", largestPalindrome(1))
	fmt.Println(" 987 -> ", largestPalindrome(2))
	fmt.Println("123 -> ", largestPalindrome(3))
	fmt.Println(" 597 -> ", largestPalindrome(4))
	fmt.Println(" 677 -> ", largestPalindrome(5))
	fmt.Println(" 1218 -> ", largestPalindrome(6))
	fmt.Println(" 877 -> ", largestPalindrome(7))
	fmt.Println(" 475 -> ", largestPalindrome(8))
}
