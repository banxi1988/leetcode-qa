package main

import (
	"fmt"
)

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func reverse(arr []int) {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
}

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	digits := []int{}
	absnum := abs(num)
	for absnum > 0 {
		digit := absnum % 7
		absnum = absnum / 7
		digits = append(digits, digit)
	}
	reverse(digits)
	bytes := make([]byte, len(digits))
	for index := 0; index < len(digits); index++ {
		digit := digits[index]
		char := byte(digit) + '0'
		bytes[index] = char
	}
	if num < 0 {
		bytes = append([]byte{'-'}, bytes...)
	}
	return string(bytes)
}

func main() {
	fmt.Println("202 -> ", convertToBase7(100))
	fmt.Println("-10 -> ", convertToBase7(-7))
	fmt.Println("0 -> ", convertToBase7(0))
}
