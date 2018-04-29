package main

import "fmt"
import "math"

func twosComplement(num int) int {
	mask := int(math.Pow(2, 32-1))
	return (num & mask) + (num & ^mask)
}

func toHex(num int) string {
	hexChars := []byte{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
	digits := []byte{}
	for index := 0; index < 8; index++ {
		digit := 0xf & num
		num = num >> 4
		char := hexChars[digit]
		digits = append([]byte{char}, digits...)
		if num == 0 {
			break
		}
	}
	return string([]byte(digits))
}

func main() {
	fmt.Println("a ->", toHex(10))
	fmt.Println("10 ->", toHex(16))
	fmt.Println("1a ->", toHex(26))
	fmt.Println("1b ->", toHex(27))
	fmt.Println("400 ->", toHex(1024))
	fmt.Println("ffffffff ->", toHex(-1))
}
