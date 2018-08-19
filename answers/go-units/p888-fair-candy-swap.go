package leetcode

func sum(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	return s
}

func fairCandySwap(A []int, B []int) []int {
	sugarA := sum(A)
	sugarB := sum(B)
	if sugarA > sugarB {
		diff := (sugarA - sugarB)/2
		for i := 0; i < len(A); i++ {
			for j := 0; j < len(B); j++ {
				if A[i]-B[j] == diff {
					return []int{A[i], B[j]}
				}
			}
		}
	} else {
		diff := (sugarB - sugarA)/2
		for i := 0; i < len(B); i++ {
			for j := 0; j < len(A); j++ {
				if B[i]-A[j] == diff {
					return []int{A[j], B[i]}
				}
			}
		}
	}
	return []int{}
}
