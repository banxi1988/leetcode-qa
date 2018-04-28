package main

import "fmt"
import "math"
import "strconv"

func findNthDigit(n int) int {
	exp := 0
	multiple := 1
	base := 0
	remain := n
	for remain > base {
		remain -= base
		base = 9 * int(math.Pow10(exp)) * multiple
		multiple++
		exp++
	}
	multiple--
	exp--
	numBase := int(math.Pow10(exp))
	numIndex := int(math.Ceil(float64(remain) / float64(multiple)))
	digitIndex := multiple - (numIndex*multiple - remain) - 1
	num := numBase + numIndex - 1
	// fmt.Println("<<<<<<<<<", remain, base, exp, multiple, num, digitIndex)
	numStr := strconv.Itoa(num)
	digit, _ := strconv.Atoi(string(rune(numStr[digitIndex])))
	return digit

}

func main() {
	fmt.Println("3", findNthDigit(3))
	fmt.Println("0", findNthDigit(11))
	fmt.Println("1", findNthDigit(12))
	fmt.Println("1", findNthDigit(13))
	fmt.Println("1", findNthDigit(14))
	fmt.Println("2", findNthDigit(15))
	fmt.Println("1", findNthDigit(16))
	fmt.Println("3", findNthDigit(17))
	fmt.Println("9", findNthDigit(9))    // 9
	fmt.Println("9", findNthDigit(188))  // 99
	fmt.Println("9", findNthDigit(189))  // 99
	fmt.Println("9", findNthDigit(2889)) // 999
}
