package main

import (
	"fmt"
	"time"
)

func canConstruct(ransomNote string, magazine string) bool {
	if len(magazine) < len(ransomNote) {
		return false
	}
	dict := make(map[rune]int)
	for _, byt := range magazine {
		count, _ := dict[byt]
		dict[byt] = count + 1
	}
	for _, ch := range ransomNote {
		count, ok := dict[ch]
		if !ok || count < 1 {
			return false
		}
		dict[ch] = count - 1
	}
	return true
}

func main() {
	start := time.Now()
	fmt.Println(" false  -> ", canConstruct("a", "b"))
	fmt.Println(" false  -> ", canConstruct("aa", "ab"))
	fmt.Println(" true  -> ", canConstruct("aa", "aab"))
	fmt.Println(" true ->", canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))
	elapsed := time.Since(start)
	fmt.Println("elapsed: ", elapsed)
}
