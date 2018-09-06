package gmedium

import "strings"

func findBaseAndSymbol(num int) (int, string) {
	if num >= 1000 {
		return 1000, "M"
	} else if num >= 900 {
		return 900, "CM"
	} else if num >= 500 {
		return 500, "D"
	} else if num >= 400 {
		return 400, "CD"
	} else if num >= 100 {
		return 100, "C"
	} else if num >= 90 {
		return 90, "XC"
	} else if num >= 50 {
		return 50, "L"
	} else if num >= 40 {
		return 40, "XL"
	} else if num >= 10 {
		return 10, "X"
	} else if num >= 9 {
		return 9, "IX"
	} else if num >= 5 {
		return 5, "V"
	} else if num >= 4 {
		return 4, "IV"
	} else {
		return 1, "I"
	}
}

func intToRoman(num int) string {
	base, symbol := findBaseAndSymbol(num)
	count := num / base
	remain := num - base*count
	if remain == 0 {
		return strings.Repeat(symbol, count)
	}
	return strings.Repeat(symbol, count) + intToRoman(remain)
}
