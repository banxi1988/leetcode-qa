package main

import "fmt"
import "unicode"

func countSegments(s string) int {
	wordCount := 0
	wordStart := false
	for _, char := range s {
		if unicode.IsLetter(char) {
			wordStart = true
		} else {
			if wordStart {
				if char == '\'' || char == '-' {
					continue
				} else {
					wordCount++
					wordStart = false
				}
			}
		}
	}
	if wordStart {
		wordCount++
	}
	return wordCount
}

func main() {
	fmt.Println("5 -> ", countSegments("Hello, my name is John"))
	fmt.Println("4 ->", countSegments("love live! mu'sic forever"))
	fmt.Println("6", countSegments(", , , ,        a, eaefa"))
}
