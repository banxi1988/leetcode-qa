package main

import "fmt"
import "strings"

func wordPattern(pattern, str string) bool {
	charCount := len(pattern)
	parts := strings.Split(str, " ")
	if charCount != len(parts) {
		return false
	}
	charPartMap := make(map[byte]string)
	partCharMap := make(map[string]byte)
	for i := 0; i < charCount; i++ {
		part := parts[i]
		char := pattern[i]
		oldPart, exists := charPartMap[char]
		if exists {
			if oldPart != part {
				return false
			}
		} else {
			charPartMap[char] = part
		}

		oldChar, ok := partCharMap[part]
		if ok {
			if oldChar != char {
				return false
			}
		} else {
			partCharMap[part] = char
		}
	}
	return true
}

func main() {
	fmt.Println("true -> ", wordPattern("abba", "dog cat cat dog"))
	fmt.Println("false -> ", wordPattern("abba", "dog cat cat fish"))
	fmt.Println("false -> ", wordPattern("aaaa", "dog cat cat dog"))
	fmt.Println("false -> ", wordPattern("abba", "dog dog dog dog"))
}
