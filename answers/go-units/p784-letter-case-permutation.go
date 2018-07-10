package leetcode

func letterCasePermutation(S string) []string {
	letters := []byte(S)
	charsIndex := []int{}
	for i := 0; i < len(letters); i++ {
		char := letters[i]
		if (char >= 'A' && char <= 'Z') || (char >= 'a' && char <= 'z') {
			charsIndex = append(charsIndex, i)
		}
	}
	// combination
	// 用二进制来表示组件形式，因为最多只有 12 个字符。所以可以使用二进制。
	// 比如只有两个字母的情况 ab
	// a -> 01
	// b -> 10
	// ab -> 11
	// 所以这样可以用二进制位，表示 C(n,m) 的所有情况
	charCount := len(charsIndex)
	endBitNum := 1 << uint(charCount)
	results := []string{}
	for i := 0; i < endBitNum; i++ {
		charIndexComp := []int{}
		for k := 0; k < charCount; k++ {
			if (i>>uint(k))&0x1 == 1 {
				charIndexComp = append(charIndexComp, charsIndex[k])
			}
		}

		bytes := []byte(S)
		for _, charIndex := range charIndexComp {
			char := bytes[charIndex]
			if char >= 'a' {
				// to Upper
				bytes[charIndex] = (char - 'a') + 'A'
			} else {
				// to lower
				bytes[charIndex] = (char - 'A') + 'a'
			}
		}
		results = append(results, string(bytes))

	}
	return results
}
