package main

import "fmt"
import "strconv"

func compress(chars []byte) int {
	var prevChar byte
	prevChar = 0
	charCount := 0
	compressIndex := 0

	writeCompressedChars := func() {
		chars[compressIndex] = prevChar
		digitBytes := []byte(strconv.Itoa(charCount))
		for i := 0; i < len(digitBytes); i++ {
			compressIndex++
			chars[compressIndex] = digitBytes[i]
		}
	}

	for i := 0; i < len(chars); i++ {
		ch := chars[i]
		if ch == prevChar {
			charCount++
		} else {
			if charCount > 0 {
				if charCount > 1 {
					writeCompressedChars()
				} else {
					chars[compressIndex] = prevChar
				}
				compressIndex++
			}
			prevChar = ch
			charCount = 1
		}
	}

	if charCount > 0 {
		if charCount > 1 {
			writeCompressedChars()
		} else {
			chars[compressIndex] = prevChar
		}
	}
	return compressIndex + 1
}

func main() {
	bytes1 := []byte{'a'}
	fmt.Println("1 -> ", compress(bytes1))
	fmt.Println(bytes1)

	bytes2 := []byte("aabbccc")
	fmt.Println("6 -> ", compress(bytes2))
	fmt.Println(bytes2)

	bytes3 := []byte("abbbbbbbbbbbb")
	fmt.Println("4 -> ", compress(bytes3))
	fmt.Println(bytes3)

	bytes4 := []byte("aaaaaaaaaa")
	fmt.Println("3 -> ", compress(bytes4))
	fmt.Println(bytes4)
}
