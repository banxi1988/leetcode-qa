package main

import (
	"fmt"
)

func reverseArray(nums []byte) {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		tmp := nums[i]
		nums[i] = nums[j]
		nums[j] = tmp
	}
}

func reverseWords(s string) string {
	letters := []byte(s)
	letterCount := len(letters)
	wordStart := 0
	for i := 0; i < letterCount; i++ {
		letter := letters[i]
		if letter == ' ' {
			if i > 0 {
				reverseArray(letters[wordStart:i])
			}
			wordStart = i + 1
		}
	}
	if wordStart < letterCount {
		reverseArray(letters[wordStart:letterCount])
	}
	return string(letters)
}

func main() {
	fmt.Println("s'teL ekat edoCteeL tsetnoc ->", reverseWords("Let's take LeetCode contest"))
}
