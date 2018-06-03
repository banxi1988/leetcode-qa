package main

import (
	"fmt"
)

func editedString(str string) string {
	bytes := []byte(str)
	result := []byte{}
	for i := 0; i < len(bytes); i++ {
		ch := bytes[i]
		rlen := len(result)
		if ch == '#' {
			if rlen > 0 {
				result = result[:rlen-1]
			}
		} else {
			result = append(result, ch)
		}
	}
	return string(result)
}

func backspaceCompare(S string, T string) bool {
	s1 := editedString(S)
	s2 := editedString(T)
	return s1 == s2
}

func main() {
	fmt.Println("true -> ", backspaceCompare("ab#c", "ad#c"))
	fmt.Println("true -> ", backspaceCompare("ab##", "c#d#"))
	fmt.Println("true -> ", backspaceCompare("a##c", "#a#c"))
	fmt.Println("false -> ", backspaceCompare("a#c", "b"))
	fmt.Println("false -> ", backspaceCompare("a##", "b"))
}
