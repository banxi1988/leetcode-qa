package gmedium

func sumSubarrayMins(A []int) int {
	result := 0
	MAX := 1000000007
	numCount := len(A)
	minBeforeI := make([]int, numCount)
	min := 3000001
	for i := 0; i < numCount; i++ {
		num := A[i]
		if num < min {
			min = num
		}
		minBeforeI[i] = min
	}
	for i := 0; i < numCount; i++ {
		min := A[i]
		result += min
		for j := i + 1; j < numCount; j++ {
			cur := A[j]
			if cur < min {
				min = cur
			}
			result += min
		}
	}
	return result % MAX
}
