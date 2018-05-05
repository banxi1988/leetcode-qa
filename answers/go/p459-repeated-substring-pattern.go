package main

import "fmt"

func isMatch(p1, p2 []byte) bool {
	len1 := len(p1)
	len2 := len(p2)
	if len1 != len2 {
		return false
	}
	for i := 0; i < len1; i++ {
		if p1[i] != p2[i] {
			return false
		}
	}
	return true
}

func repeatedSubstringPattern(s string) bool {
	sbytes := []byte(s)
	slen := len(sbytes)
	if slen < 2 {
		return false
	}
	for plen := 1; plen < (slen - plen + 1); plen++ {
		if (slen % plen) != 0 {
			continue
		}
		pattern := sbytes[0:plen]
		allMatch := true
		for i := plen; i < (slen - plen + 1); i += plen {
			subbytes := sbytes[i : i+plen]
			if !isMatch(pattern, subbytes) {
				allMatch = false
				break
			}
		}
		if allMatch {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println("false ->", repeatedSubstringPattern("a"))
	fmt.Println("true ->", repeatedSubstringPattern("aa"))
	fmt.Println("true ->", repeatedSubstringPattern("aaa"))
	fmt.Println("true ->", repeatedSubstringPattern("abab"))
	fmt.Println("false ->", repeatedSubstringPattern("abc"))
	fmt.Println("true ->", repeatedSubstringPattern("abcabcabcabc"))
	fmt.Println("true ->", repeatedSubstringPattern("abcabcabcabcabcabc"))
}
