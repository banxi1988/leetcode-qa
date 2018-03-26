package main

import "fmt"

func isPalindrome(s string) bool {
	validBytes := []byte{}
	for _, byt := range []byte(s) {
		isDigit := byt >= '0' && byt <= '9'
		isLower := (byt >= 'a' && byt <= 'z')
		isUpper := (byt >= 'A' && byt <= 'Z')
		if isDigit || isLower {
			validBytes = append(validBytes, byt)
		} else if isUpper {
			lower := byt - 'A' + 'a'
			validBytes = append(validBytes, lower)
		}
	}
	bytesCount := len(validBytes)
	if bytesCount == 0 {
		return true
	}
	for start, end := 0, bytesCount-1; start < end; start, end = start+1, end-1 {
		if validBytes[start] != validBytes[end] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("true -> ", isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println("false -> ", isPalindrome("race a car"))
	fmt.Println("true -> ", isPalindrome("rar"))
	fmt.Println("true -> ", isPalindrome(""))
	fmt.Println("true -> ", isPalindrome("zbAaBZ"))
}
