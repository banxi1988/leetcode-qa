package main

import "fmt"

func licenseKeyFormatting(S string, K int) string {
	bytes := []byte(S)
	alphanums := make([]byte, 0, len(bytes))
	ulchOffset := byte('a' - 'A')
	for i := 0; i < len(bytes); i++ {
		ch := bytes[i]
		if ch == '-' {
			continue
		} else if ch >= 'a' {
			ch = ch - ulchOffset
		}
		alphanums = append(alphanums, ch)
	}
	alphanumsLen := len(alphanums)
	if alphanumsLen <= K {
		return string(alphanums)
	}
	offset := alphanumsLen % K
	resultBytes := make([]byte, 0, len(bytes))
	if offset > 0 {
		resultBytes = append(resultBytes, alphanums[0:offset]...)
	}
	for (offset + K) <= alphanumsLen {
		if offset > 0 {
			resultBytes = append(resultBytes, '-')
		}
		resultBytes = append(resultBytes, alphanums[offset:offset+K]...)
		offset += K
	}
	return string(resultBytes)
}

func main() {
	fmt.Println("5F3Z-2E9W -> ", licenseKeyFormatting("5F3Z-2e-9-w", 4))
	fmt.Println("2-5G-3J -> ", licenseKeyFormatting("2-5g-3-J", 2))
	fmt.Println("2-5GA-3JB -> ", licenseKeyFormatting("2-5ga-3-Jb", 3))
}
