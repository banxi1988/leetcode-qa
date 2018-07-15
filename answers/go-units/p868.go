package leetcode

func binaryGap(N int) int {
	bits := []int{}
	num := N
	for num > 0 {
		if num&0x1 == 1 {
			bits = append(bits, 1)
		} else {
			bits = append(bits, 0)
		}
		num = num >> 1
	}
	maxLen := 0
	prevIndex := -1
	for i := 0; i < len(bits); i++ {
		bit := bits[i]
		if bit == 0 {
			continue
		}
		if prevIndex != -1 {
			curLen := i - prevIndex
			if curLen > maxLen {
				maxLen = curLen
			}
		}
		prevIndex = i
	}
	return maxLen
}
