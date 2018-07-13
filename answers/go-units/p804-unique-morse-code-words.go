package leetcode

import (
	"strings"
)

func uniqueMorseRepresentations(words []string) int {
	morsecodes := [26]string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	codeSet := make(map[string]bool)
	for _, word := range words {
		chars := []byte(word)
		codes := make([]string, len(chars))
		for i, ch := range chars {
			codeIndex := ch - 'a'
			moresecode := morsecodes[codeIndex]
			codes[i] = moresecode
		}
		str := strings.Join(codes, "")
		codeSet[str] = true
	}
	return len(codeSet)
}
