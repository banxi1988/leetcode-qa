package main

import (
	"fmt"
	"sort"
)

func contains(words []string, word string) bool {
	for _, w := range words {
		if w == word {
			return true
		}
	}
	return false
}

func canBuiltWord(dict map[int][]string, word string) bool {
	curLen := len(word)
	lenWords, _ := dict[curLen]
	if contains(lenWords, word) {
		if curLen == 1 {
			return true
		}
		return canBuiltWord(dict, word[0:len(word)-1])
	}
	return false
}

func longestWord(words []string) string {
	lenWordsMap := make(map[int][]string)
	maxLen := 0
	for i := 0; i < len(words); i++ {
		word := words[i]
		curLen := len(word)
		lenWords, _ := lenWordsMap[curLen]
		lenWords = append(lenWords, word)
		lenWordsMap[curLen] = lenWords
		if curLen > maxLen {
			maxLen = curLen
		}
	}
	for ; maxLen > 0; maxLen-- {
		lenWords, _ := lenWordsMap[maxLen]
		longestWords := []string{}
		if maxLen == 1 {
			longestWords = lenWords
		} else {
			for i := 0; i < len(lenWords); i++ {
				word := lenWords[i]
				if canBuiltWord(lenWordsMap, word[0:len(word)-1]) {
					longestWords = append(longestWords, word)
				}
			}
		}
		if len(longestWords) > 0 {
			if len(longestWords) > 1 {
				sort.Strings(longestWords)
			}
			return longestWords[0]
		}
	}
	return ""
}

func main() {
	arr1 := []string{"w", "wo", "wor", "worl", "world"}
	fmt.Println("world ->", longestWord(arr1))
	arr2 := []string{"a", "banana", "app", "appl", "ap", "apply", "apple"}
	fmt.Println("apple ->", longestWord(arr2))

	arr3 := []string{"ts", "e", "x", "pbhj", "opto", "xhigy", "erikz", "pbh", "opt", "erikzb", "eri", "erik", "xlye", "xhig", "optoj", "optoje", "xly", "pb", "xhi", "x", "o"}
	fmt.Println("e ->", longestWord(arr3))
}
