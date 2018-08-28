package gmedium

func isPalindrom(bytes []byte) bool {
	for i, j := 0, len(bytes)-1; i < j; i, j = i+1, j-1 {
		if bytes[i] != bytes[j] {
			return false
		}
	}
	return true
}

func longestPalindrome(s string) string {
	byteArr := []byte(s)
	byteCount := len(byteArr)
	longest := []byte{}
	for start := 0; start < byteCount; start++ {
		for end := byteCount; end >= (start + len(longest)); end-- {
			slice := byteArr[start:end]
			if len(slice) > len(longest) && isPalindrom(slice) {
				longest = slice
			}
		}
	}
	return string(longest)
}
