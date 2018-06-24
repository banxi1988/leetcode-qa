package main

import (
	"fmt"
)

func scoreOfParent(bytes []byte) int {
	charCount := len(bytes)
	if charCount == 2 {
		return 1
	} else {
		depth := 0
		matchIndex := -1
		for i := 1; i < charCount; i++ {
			if bytes[i] == ')' {
				if depth == 0 {
					matchIndex = i
					break
				} else {
					depth--
				}
			} else {
				depth++
			}
		}
		if matchIndex == 1 {
			return 1 + scoreOfParent(bytes[2:])
		} else if matchIndex == charCount-1 {
			return 2 * scoreOfParent(bytes[1:matchIndex])
		} else {
			return 2*scoreOfParent(bytes[1:matchIndex]) + scoreOfParent(bytes[matchIndex+1:])
		}
	}
}

func scoreOfParentheses(S string) int {
	return scoreOfParent([]byte(S))
}

func main() {
	fmt.Println("1 ->", scoreOfParentheses("()"))
	fmt.Println("2 ->", scoreOfParentheses("(())"))
	fmt.Println("4 ->", scoreOfParentheses("((()))"))
	fmt.Println("2 ->", scoreOfParentheses("()()"))
	fmt.Println("6 ->", scoreOfParentheses("(()(()))"))
}
