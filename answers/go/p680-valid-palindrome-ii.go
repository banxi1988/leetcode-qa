package main

import (
	"fmt"
)

func isPalindrome(bytes []byte) bool {
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		if bytes[i] != bytes[j] {
			return false
		}
	}
	return true
}

func validPalindrome(s string) bool {
	bytes := []byte(s)
	unmatchCount := 0
	// pass j
	for i, j := 0, len(bytes)-1; i < j; {
		if bytes[i] != bytes[j] {
			unmatchCount++
			if unmatchCount > 1 {
				break
			}
			// pass j
			j--
		} else {
			i++
			j--
		}
	}
	if unmatchCount < 2 {
		return true
	}
	unmatchCount = 0
	// pass i
	for i, j := 0, len(bytes)-1; i < j; {
		if bytes[i] != bytes[j] {
			unmatchCount++
			if unmatchCount > 1 {
				break
			}
			// pass i
			i++
		} else {
			i++
			j--
		}
	}
	return unmatchCount < 2
}

func main() {
	fmt.Println("true -> ", validPalindrome("aba"))
	fmt.Println("true -> ", validPalindrome("abca"))
	fmt.Println("true -> ", validPalindrome("abcb"))
	fmt.Println("true -> ", validPalindrome("abbcba"))
}
