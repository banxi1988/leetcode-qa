package leetcode

func longestIncreasingSubsequence(A []int) int {
	d := make([]int, len(A))
	maxLen := 1
	for i := 0; i < len(A); i++ {
		d[i] = 1
		for j := 0; j < i; j++ {
			if A[j] <= A[i] && d[j]+1 > d[i] {
				d[i] = d[j] + 1
			}
		}
		if d[i] > maxLen {
			maxLen = d[i]
		}
	}
	return maxLen
}
