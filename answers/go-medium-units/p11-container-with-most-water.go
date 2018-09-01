package gmedium

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func mini(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	calcArea := func(i, j int) int {
		w := abs(i - j)
		h := mini(height[i], height[j])
		return w * h
	}
	lineCount := len(height)
	maxArea := 0
	for i, j := 0, lineCount-1; i < j; {
		area := calcArea(i, j)
		if area > maxArea {
			maxArea = area
		}
		if height[i] < height[j] {
			i++
		} else {
			j--
		}
	}

	return maxArea
}
