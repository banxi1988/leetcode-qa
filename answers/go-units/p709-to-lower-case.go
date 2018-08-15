package leetcode

func toLowerCase(str string) string {
	bytes := []byte(str)
	for i, ch := range bytes {
		if ch >= 'A' && ch <= 'Z' {
			lower := ch - 'A' + 'a'
			bytes[i] = lower
		}
	}
	return string(bytes)
}
