package leetcode

import (
	"bytes"
)

func shortestToChar(S string, C byte) []int {
	chars := []byte(S)
	result := make([]int, len(chars))
	for i, ch := range chars {
		if ch == C {
			result[i] = 0
		} else {
			leftSlice := chars[0:i]
			rightSlice := chars[i+1:]
			leftIndex := bytes.LastIndexByte(leftSlice, C)
			rightIndex := bytes.IndexByte(rightSlice, C)
			leftDistance := i - leftIndex
			rightDistance := rightIndex + 1
			if leftIndex != -1 && rightIndex != -1 {
				if leftDistance > rightDistance {
					result[i] = rightDistance
				} else {
					result[i] = leftDistance
				}
			} else {
				if rightIndex != -1 {
					result[i] = rightDistance
				} else {
					result[i] = leftDistance
				}
			}
		}
	}
	return result
}
