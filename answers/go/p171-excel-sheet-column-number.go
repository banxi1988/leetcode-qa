package main

import "fmt"

func titleToNumber(s string) int {
	columnNo := 0
	base := 1
	for i := len(s) - 1; i > -1; i-- {
		letter := s[i]
		no := int(letter - 'A' + 1)
		columnNo += (no * base)
		base *= 26
	}
	return columnNo
}

func main() {
	fmt.Println("A -> 1 ", titleToNumber("A"))
	fmt.Println("B -> 2 ", titleToNumber("B"))
	fmt.Println("Z -> 26 ", titleToNumber("Z"))
	fmt.Println("AA -> 27 ", titleToNumber("AA"))
	fmt.Println("AB -> 28 ", titleToNumber("AB"))
	fmt.Println("ZZ -> 702 ", titleToNumber("ZZ"))
	fmt.Println("AAA -> 703 ", titleToNumber("AAA"))
}
