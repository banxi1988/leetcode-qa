package leetcode

func numberOfLines(widths []int, S string) []int {
	chars := []byte(S)
	charCount := len(chars)
	i := 0
	lineCount := 1
	lineUsedUnit := 0
	const maxWidth = 100
	for i < charCount {
		charIndex := chars[i] - 'a'
		width := widths[charIndex]
		if (lineUsedUnit + width) > maxWidth {
			lineCount++
			lineUsedUnit = width
		} else {
			lineUsedUnit += width
		}
		i++
	}
	return []int{lineCount, lineUsedUnit}
}
