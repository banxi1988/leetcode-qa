package main

import "fmt"

import "strings"

func maskEmail(email string) string {
	normalEmail := strings.ToLower(email)
	parts := strings.Split(normalEmail, "@")
	name := parts[0]
	nameLen := len(name)
	bytes := []byte{}
	bytes = append(bytes, name[0])
	bytes = append(bytes, []byte("*****")...)
	bytes = append(bytes, name[nameLen-1])
	bytes = append(bytes, '@')
	bytes = append(bytes, []byte(parts[1])...)
	return string(bytes)
}

func maskPhoneNumber(phone string) string {
	// 1) extract digits
	strBytes := []byte(phone)
	digits := []byte{}
	for i := 0; i < len(strBytes); i++ {
		char := strBytes[i]
		if char >= '0' && char <= '9' {
			digits = append(digits, char)
		}
	}

	maskedBytes := []byte{}
	countryCodeLen := len(digits) - 10
	// has country
	if countryCodeLen > 0 {
		switch countryCodeLen {
		case 1:
			maskedBytes = append(maskedBytes, []byte("+*-")...)
		case 2:
			maskedBytes = append(maskedBytes, []byte("+**-")...)
		case 3:
			maskedBytes = append(maskedBytes, []byte("+***-")...)
		default:
			break
		}
	}
	maskedBytes = append(maskedBytes, []byte("***-***-")...)
	exposedDigits := digits[len(digits)-4 : len(digits)]
	maskedBytes = append(maskedBytes, exposedDigits...)
	return string(maskedBytes)
}

func maskPII(S string) string {
	if strings.Contains(S, "@") {
		return maskEmail(S)
	} else {
		return maskPhoneNumber(S)
	}
}

func main() {
	fmt.Println("a*****b@qq.com ->", maskPII("AB@qq.com"))
	fmt.Println("***-***-7890->", maskPII("1(234)567-890"))
	fmt.Println("+**-***-***-5678", maskPII("86-(10)12345678"))
}
