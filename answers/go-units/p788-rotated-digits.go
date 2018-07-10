package leetcode

func checkAndRotateNumber(num int) (bool, int) {
	origNum := num
	rotatedNum := 0
	base := 1
	for num > 0 {
		digit := num % 10

		rotatedDigit := digit
		switch digit {
		case 0, 1, 8:
			break
		case 2:
			rotatedDigit = 5
		case 5:
			rotatedDigit = 2
		case 6:
			rotatedDigit = 9
		case 9:
			rotatedDigit = 6
		default:
			return false, 0
		}
		rotatedNum += rotatedDigit * base
		base *= 10
		num /= 10
	}
	return rotatedNum != origNum, rotatedNum
}

func rotatedDigits(N int) int {
	count := 0
	for num := 1; num <= N; num++ {
		valid, _ := checkAndRotateNumber(num)
		if valid {
			count++
		}
	}
	return count
}
