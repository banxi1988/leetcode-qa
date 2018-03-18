package main

import "fmt"

func lengthOfLastWord(s string) int {
	chars := []rune(s)
	lastWordLen := 0
	currentWordLen := 0
	for i := 0; i < len(chars); i++ {
		ch := chars[i]
		if ch == ' ' {
			if currentWordLen > 0 {
				lastWordLen = currentWordLen
				currentWordLen = 0
			}
			continue
		}
		currentWordLen++
	}
	if currentWordLen > 0 {
		return currentWordLen
	}
	return lastWordLen
}

func main() {
	fmt.Println("1 ", lengthOfLastWord("a"))
	fmt.Println("1 ", lengthOfLastWord("a "))
	fmt.Println("1 ", lengthOfLastWord("b  a  "))
	fmt.Println("2 ", lengthOfLastWord("ab abc aa "))
	fmt.Println("5 ", lengthOfLastWord("Hello World"))
	fmt.Println("3 ", lengthOfLastWord("Today is a nice day"))
}
