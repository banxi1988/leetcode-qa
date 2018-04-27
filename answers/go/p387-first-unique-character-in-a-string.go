package main

import "fmt"

func firstUniqChar(s string) int {
	dict := make(map[rune]int)
	for _, ch := range s {
		count, _ := dict[ch]
		dict[ch] = count + 1
	}

	for index, ch := range s {
		count, _ := dict[ch]
		if count == 1 {
			return index
		}
	}
	return -1
}

func main() {
	fmt.Println("0  -> ", firstUniqChar("leetcode"))
	fmt.Println("2  -> ", firstUniqChar("loveleetcode"))
}
