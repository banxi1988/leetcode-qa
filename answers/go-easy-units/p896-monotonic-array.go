package geasy

func isMonoInc(arr []int) bool {
	for i, j := 0, 1; j < len(arr); i, j = i+1, j+1 {
		if arr[i] > arr[j] {
			return false
		}
	}
	return true
}

func isMonoDec(arr []int) bool {
	for i, j := 0, 1; j < len(arr); i, j = i+1, j+1 {
		if arr[i] < arr[j] {
			return false
		}
	}
	return true
}

func isMonotonic(A []int) bool {
	if len(A) < 2 {
		return true
	}

	return isMonoInc(A) || isMonoDec(A)
}
