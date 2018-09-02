package gmedium

func subarrayBitwiseORs(A []int) int {
	valueMap := make(map[int]bool)
	maxValue := 0
	for i := 0; i < len(A); i++ {
		maxValue |= A[i]
	}
	valueMap[maxValue] = true

	curValue := 0
	for i := 0; i < len(A); i++ {
		curValue = A[i]
		valueMap[curValue] = true
		for j := i + 1; j < len(A); j++ {
			curValue |= A[j]
			if curValue >= maxValue {
				break
			}
			valueMap[curValue] = true
		}
	}
	return len(valueMap)
}
