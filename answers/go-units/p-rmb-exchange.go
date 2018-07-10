package leetcode

const rmbBaseCount = 6

var rmbBases = [rmbBaseCount]int{1, 5, 10, 20, 50, 100}

func fewestRmbExhcange(amount int) int {
	count := 0
	remain := amount
	for remain > 0 {
		for i := rmbBaseCount - 1; i > -1; {
			if remain >= rmbBases[i] {
				remain = remain - rmbBases[i]
				count++
			} else {
				i--
			}
		}
	}
	return count
}
