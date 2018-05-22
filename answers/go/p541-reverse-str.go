package main

import (
	"fmt"
)

func reverseArray(nums []byte) {
	for i, j := 0, len(nums)-1; i < j; i, j = i+1, j-1 {
		tmp := nums[i]
		nums[i] = nums[j]
		nums[j] = tmp
	}
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func reverseStr(s string, k int) string {
	bytes := []byte(s)
	byteCount := len(bytes)
	count := 0
	for ; count+2*k < byteCount; count += 2 * k {
		reverseArray(bytes[count : count+k])
	}
	if count < byteCount {
		endIndex := min(byteCount, count+k)
		reverseArray(bytes[count:endIndex])
	}
	return string(bytes)
}

func main() {
	fmt.Println("bacdfeg ->", reverseStr("abcdefg", 2))
}
