package main

import (
	"fmt"
)

// aab
// aba

func findNextMatchChar(chars []byte, char byte, fromIndex int) int {
	for index := fromIndex; index < len(chars); index++ {
		if chars[index] == char {
			return index
		}
	}
	return -1
}

func canChangeOneTime(bytes []byte) bool {
	degreeMap := make(map[byte]int, len(bytes))
	for _, ch := range bytes {
		degree, _ := degreeMap[ch]
		degree++
		degreeMap[ch] = degree
		if degree > 1 {
			return true
		}
	}
	return false
}

func buddyStrings(A string, B string) bool {
	charsA := []byte(A)
	charsB := []byte(B)
	charCount := len(charsA)
	if charCount != len(charsB) {
		return false
	}

	exchangeCount := 0
	for i := 0; i < charCount; i++ {
		chA := charsA[i]
		chB := charsB[i]
		if chA != chB {
			if exchangeCount > 0 {
				return false
			}
			matchIndex := findNextMatchChar(charsA, chB, i+1)
			if matchIndex != -1 {
				charsA[i] = charsA[matchIndex]
				charsA[matchIndex] = chA
				exchangeCount++
			}
		}
	}
	if exchangeCount == 0 {
		return canChangeOneTime(charsA)
	}
	return exchangeCount < 2
}
func main() {
	fmt.Println("true -> ", buddyStrings("ab", "ba"))
	fmt.Println("false -> ", buddyStrings("ab", "ab"))
	fmt.Println("true -> ", buddyStrings("aa", "aa"))
	fmt.Println("false -> ", buddyStrings("", "aa"))
	fmt.Println("true -> ", buddyStrings("aaaaaaabc", "aaaaaaacb"))
}
