package gmedium

import (
	"bytes"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	substrBytes := []byte{}
	maxLen := 0
	byteArr := []byte(s)
	for _, byt := range byteArr {
		oldIndex := bytes.IndexByte(substrBytes, byt)
		if oldIndex != -1 {
			maxLen = max(maxLen, len(substrBytes))
			substrBytes = substrBytes[oldIndex+1:]
		}
		substrBytes = append(substrBytes, byt)
	}
	maxLen = max(maxLen, len(substrBytes))
	return maxLen
}
