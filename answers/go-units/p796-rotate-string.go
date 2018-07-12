package leetcode

func rotateString(A string, B string) bool {
	lenA := len(A)
	lenB := len(B)
	if lenA != lenB {
		return false
	}
	if A == B {
		return true
	}
	achars := []byte(A)
	for i := 0; i < lenA; i++ {
		ch1 := achars[0]
		achars = achars[1:]
		achars = append(achars, ch1)
		if string(achars) == B {
			return true
		}
	}
	return false
}
