package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
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
	fmt.Println(" false  -> ", canConstruct("a", "b"))
	fmt.Println(" false  -> ", canConstruct("aa", "ab"))
	fmt.Println(" true  -> ", canConstruct("aa", "aab"))
	fmt.Println(" true ->", canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))
}
