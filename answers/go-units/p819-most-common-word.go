package leetcode

import (
	"regexp"
	"strings"
)

func mostCommonWord(paragraph string, banned []string) string {
	punctRe := regexp.MustCompile("\\W")
	words := punctRe.Split(paragraph, -1)
	bannedSet := make(map[string]bool, len(banned))
	for _, bannedWord := range banned {
		bannedSet[bannedWord] = true
	}
	wordCountMap := make(map[string]int)
	result := ""
	maxCount := 0
	for _, word := range words {
		if len(word) < 1 {
			continue
		}
		word = strings.ToLower(word)
		if bannedSet[word] {
			continue
		}
		count := wordCountMap[word]
		count++
		if count > maxCount {
			maxCount = count
			result = word
		}
		wordCountMap[word] = count
	}
	return result
}
