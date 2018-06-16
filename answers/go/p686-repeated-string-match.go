package main

import (
	"fmt"
	"strings"
)

func repeatedStringMatch(A string, B string) int {
	repeatCount := 1
	str := A
	for {
		if repeatCount > 1 && len(str) > len(B)*3 {
			return -1
		}
		if strings.Contains(str, B) {
			fmt.Println(str)
			return repeatCount
		}
		str += A
		repeatCount++
	}
	return -1
}

func main() {
	fmt.Println("3 ->", repeatedStringMatch("abcd", "cdabcdab"))
	fmt.Println("-1 -> ", repeatedStringMatch("ac", "ab"))
	fmt.Println("2 -> ", repeatedStringMatch("ac", "aca"))
	fmt.Println("1 ->", repeatedStringMatch("aaaa", "a"))
}
