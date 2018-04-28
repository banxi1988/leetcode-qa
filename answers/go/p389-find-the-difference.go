package main

import "fmt"

func findTheDifferenceRune(s string, t string) string {
	byt := findTheDifference(s, t)
	return string(rune(byt))
}
func findTheDifference(s string, t string) byte {
	map1 := make(map[byte]int)
	for _, byt := range []byte(s) {
		count, _ := map1[byt]
		map1[byt] = count + 1
	}
	for _, byt := range []byte(t) {
		count, ok := map1[byt]
		if !ok || count < 1 {
			return byt
		}
		map1[byt] = count - 1
	}
	return 0
}

func main() {
	fmt.Println("e -> ", findTheDifferenceRune("abcd", "abcde"))
	fmt.Println("e -> ", findTheDifferenceRune("abab", "ababe"))
	fmt.Println("e -> ", findTheDifferenceRune("aeab", "aeabe"))
}
