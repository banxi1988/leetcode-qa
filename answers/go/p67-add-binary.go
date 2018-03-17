package main

import "fmt"

func addBinary(a string, b string) string {
	aLen := len(a)
	bLen := len(b)
	carryCount := 0
	result := ""
	i := aLen - 1
	j := bLen - 1
	for i > -1 || j > -1 {
		ach := '0'
		if i > -1 {
			ach = rune(a[i])
		}
		bch := '0'
		if j > -1 {
			bch = rune(b[j])
		}
		if ach == '1' && bch == '1' {
			if carryCount > 0 {
				result = "1" + result
			} else {
				carryCount++
				result = "0" + result
			}
		} else if ach == '1' || bch == '1' {
			if carryCount > 0 {
				result = "0" + result
			} else {
				result = "1" + result
			}
		} else {
			if carryCount > 0 {
				result = "1" + result
				carryCount--
			} else {
				result = "0" + result
			}
		}

		i--
		j--
	}
	for carryCount > 0 {
		result = "1" + result
		carryCount--
	}
	return result
}

func main() {
	fmt.Println("0 + 0 -> 0 ", addBinary("0", "0"))
	fmt.Println("0 + 1 -> 1 ", addBinary("0", "1"))
	fmt.Println("1 + 1 -> 10 ", addBinary("1", "1"))
	fmt.Println("10 + 10 -> 100 ", addBinary("10", "10"))
	fmt.Println("100 + 10 -> 110 ", addBinary("100", "10"))
	fmt.Println("11 + 1 -> 100 ", addBinary("11", "1"))
	fmt.Println("110 + 1 -> 111 ", addBinary("110", "111"))
	fmt.Println("111 + 1 -> 1000 ", addBinary("111", "1"))
	fmt.Println("111 + 11 -> 1010 ", addBinary("111", "11"))
	fmt.Println("111 + 111 -> 1110 ", addBinary("111", "111"))
	fmt.Println("1010 + 1011 -> 10101 ", addBinary("1010", "1011"))
	fmt.Println(" -> 110100 ", addBinary("10111", "11101"))
}
