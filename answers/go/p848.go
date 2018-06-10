package main

import (
	"fmt"
)

func sum(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	return s
}

func shiftingLetters(S string, shifts []int) string {
	bytes := []byte(S)
	for i := 0; i < len(bytes); i++ {
		shiftCount := sum(shifts[i:])
		effectShift := byte(shiftCount % 26)
		ch := bytes[i]
		toch := ch + effectShift
		if toch > 'z' {
			toch = toch - 'z' - 1 + 'a'
		}
		bytes[i] = toch
	}
	return string(bytes)
}

func main() {
	fmt.Println("rpl", shiftingLetters("abc", []int{3, 5, 9}))
}
