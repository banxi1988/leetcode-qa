package leetcode

func digitsOfNumber(num int) map[int]int {
	digits := make(map[int]int)
	for num > 0 {
		digit := num % 10
		digits[digit] = digits[digit] + 1
		num = num / 10
	}
	return digits
}

func digitsCombEqual(comb1, comb2 map[int]int) bool {
	if len(comb1) != len(comb2) {
		return false
	}
	for digit, count := range comb1 {
		if comb2[digit] == count {
			continue
		} else {
			return false
		}
	}
	return true
}

func reorderedPowerOf2(N int) bool {
	allCombs := []map[int]int{}
	maxNum := 10000000000
	powerOf2 := 1
	for powerOf2 < maxNum {
		comb := digitsOfNumber(powerOf2)
		powerOf2 = powerOf2 << 1
		allCombs = append(allCombs, comb)
	}
	// fmt.Println("allCombs:", allCombs)
	digits := digitsOfNumber(N)
	for _, comb := range allCombs {
		if digitsCombEqual(digits, comb) {
			return true
		}
	}
	return false
}
