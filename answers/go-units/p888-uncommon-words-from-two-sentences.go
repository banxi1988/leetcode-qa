package leetcode

import (
	"strings"
)

func uncommonFromSentences(A string, B string) []string {
	wordsA := strings.Split(A, " ")
	wordsB := strings.Split(B, " ")

	wordsCountMap := make(map[string]int)
	for _, word := range wordsA {
		count, _ := wordsCountMap[word]
		wordsCountMap[word] = count + 1
	}
	for _, word := range wordsB {
		count, _ := wordsCountMap[word]
		wordsCountMap[word] = count + 1
	}
	result := []string{}
	for word, count := range wordsCountMap {
		if count < 2 {
			result = append(result, word)
		}
	}
	return result
}
