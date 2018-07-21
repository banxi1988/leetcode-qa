package leetcode

import (
	"bytes"
)

func isVowel(letter byte) bool {
	ch := letter
	if letter < 'Z' {
		// to lowercase
		ch = ch - 'A' + 'a'
	}
	return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'
}
func toGoatLatin(S string) string {
	result := ""
	chars := []byte(S)
	wordCount := 0
	word := []byte{}
	processWord := func(word []byte) {
		if !isVowel(word[0]) {
			ch1 := word[0]
			word = word[1:]
			word = append(word, ch1)
		}
		word = append(word, 'm', 'a')
		word = append(word, bytes.Repeat([]byte{'a'}, wordCount)...)
		if wordCount > 1 {
			result += " "
		}
		result += string(word)
	}
	for _, ch := range chars {
		if ch == ' ' {
			wordCount++
			processWord(word)
			word = []byte{}
		} else {
			word = append(word, ch)
		}
	}
	if len(word) > 0 {
		wordCount++
		processWord(word)
	}

	return result
}
