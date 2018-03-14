package main

import "fmt"

func strStr(haystack, needle string) int {
	hayLen := len(haystack)
	needleLen := len(needle)
	if needleLen == 0 {
		return 0
	}
	if hayLen < needleLen {
		return -1
	}
	for i := 0; i < (hayLen - needleLen + 1); i++ {
		allEqual := true
		for needleIndex := 0; needleIndex < needleLen; needleIndex++ {
			hayIndex := i + needleIndex
			if haystack[hayIndex] != needle[needleIndex] {
				allEqual = false
				break
			}
		}
		if allEqual {
			return i
		}
	}
	return -1
}

func main() {
	fmt.Println(`haystack = "hello", needle = "ll" -> 2`, strStr("hello", "ll"))
	fmt.Println(`haystack = "aaaaa", needle = "bba" -> -1`, strStr("aaaaa", "bba"))
	fmt.Println(`haystack = "a", needle = "a" -> 0`, strStr("a", "a"))
	fmt.Println(`haystack = "a", needle = "" -> 0`, strStr("a", ""))
	fmt.Println(`haystack = "", needle = "a" -> -1`, strStr("", "a"))
	fmt.Println(`haystack = "a", needle = "ab" -> -1`, strStr("a", "ab"))
}
