package geasy

func numSubarraysWithSum(A []int, S int) int {
	count := len(A)
	result := 0
	for i := 0; i < count; i++ {
		sum := 0
		for j := i; j < count; j++ {
			sum += A[j]
			if sum == S {
				result++
			} else if sum > S {
				break
			}
		}
	}
	return result
}
