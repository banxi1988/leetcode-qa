package leetcode

var rmbBases = [...]int{1, 2, 5, 10, 20, 50, 100}

const rmbBaseCount = len(rmbBases)

// FewestRmbExhcange 返回最小的找零方案
func FewestRmbExhcange(amount int) []int {
	exchanges := []int{}
	remain := amount

	for remain > 0 {
		for i := rmbBaseCount - 1; i > -1; {
			base := rmbBases[i]
			if remain >= base {
				remain = remain - base
				exchanges = append(exchanges, base)
			} else {
				i--
			}
		}
	}
	return exchanges
}
