package main

import "fmt"

func btoi(char byte) int {
	switch char {
	case '0':
		return 0
	case '1':
		return 1
	case '2':
		return 2
	case '3':
		return 3
	case '4':
		return 4
	case '5':
		return 5
	case '6':
		return 6
	case '7':
		return 7
	case '8':
		return 8
	case '9':
		return 9
	default:
		panic("unkown digit char")
	}
}

func itob(digit int) byte {
	switch digit {
	case 0:
		return '0'
	case 1:
		return '1'
	case 2:
		return '2'
	case 3:
		return '3'
	case 4:
		return '4'
	case 5:
		return '5'
	case 6:
		return '6'
	case 7:
		return '7'
	case 8:
		return '8'
	case 9:
		return '9'
	default:
		panic("unkown digit")
	}
}

func addStrings(num1, num2 string) string {
	digitBytes := []byte{}
	num1Len := len(num1)
	num2Len := len(num2)
	carry := 0
	digit1 := 0
	digit2 := 0
	for i, j := (num1Len - 1), (num2Len - 1); i > -1 || j > -1; i, j = i-1, j-1 {
		digit1 = 0
		digit2 = 0
		if i > -1 {
			digit1 = btoi(num1[i])
		}
		if j > -1 {
			digit2 = btoi(num2[j])
		}

		digit := digit1 + digit2 + carry
		addSum := digit % 10
		if digit > 9 {
			carry = 1
		} else {
			carry = 0
		}
		digitByte := itob(addSum)
		digitBytes = append([]byte{digitByte}, digitBytes...)
	}
	if carry > 0 {
		digitBytes = append([]byte{'1'}, digitBytes...)
	}

	return string(digitBytes)

}

func main() {
	fmt.Println((456 + 456), "->", addStrings("456", "456"))
	fmt.Println((45 + 456), "->", addStrings("45", "456"))
	fmt.Println((4 + 456), "->", addStrings("4", "456"))
	fmt.Println((0 + 0), "->", addStrings("0", "0"))
}
