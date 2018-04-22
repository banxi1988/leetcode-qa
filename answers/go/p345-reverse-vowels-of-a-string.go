package main

import "fmt"

func IsVowel(byt byte) bool {
	lowByte := byt
	if byt < 'a' {
		lowByte = byt + ('a' - 'A')
		fmt.Println(lowByte)
	}
	// aeiou
	switch lowByte {
	case 'a', 'e', 'i', 'o', 'u':
		return true
	default:
		return false
	}
}

func reverseVowels(s string) string {
	bytes := []byte(s)
	i, j := 0, len(bytes)-1
	for i < j {
		chi := bytes[i]
		chj := bytes[j]
		iVowl := IsVowel(chi)
		jVowl := IsVowel(chj)
		if iVowl && jVowl {
			bytes[i] = chj
			bytes[j] = chi
			i++
			j--
		} else {
			if !iVowl {
				i++
			}
			if !jVowl {
				j--
			}
		}
	}
	return string(bytes)
}

func main() {
	fmt.Println("true ", IsVowel('a'))
	fmt.Println("true ", IsVowel('i'))
	fmt.Println("true ", IsVowel('o'))
	fmt.Println("true ", IsVowel('u'))
	fmt.Println("true ", IsVowel('e'))
	fmt.Println("true ", IsVowel('A'))
	fmt.Println("true ", IsVowel('I'))
	fmt.Println("true ", IsVowel('O'))
	fmt.Println("true ", IsVowel('U'))
	fmt.Println("true ", IsVowel('E'))
	fmt.Println("holle -> ", reverseVowels("hello"))
	fmt.Println("aA -> ", reverseVowels("Aa"))
	fmt.Println("leotcede -> ", reverseVowels("leetcode"))
}
