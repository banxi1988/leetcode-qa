package main

import "fmt"

func longestPalindrome(s string) int {
	charMap := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		char := s[i]
		count, _ := charMap[char]
		charMap[char] = count + 1
	}
	singleCharCount := 0
	maxLen := 0
	for _, count := range charMap {
		if count > 1 {
			maxLen += count / 2 * 2
			if count%2 != 0 {
				singleCharCount++
			}
		} else {
			singleCharCount++
		}
	}
	if singleCharCount > 0 {
		maxLen++
	}

	return maxLen
}

func main() {
	fmt.Println("7", longestPalindrome("abccccdd"))
	fmt.Println("1", longestPalindrome("a"))
	fmt.Println("2", longestPalindrome("aa"))
	fmt.Println("1", longestPalindrome("abc"))
}
