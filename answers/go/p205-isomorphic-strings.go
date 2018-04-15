package main

import "fmt"

func isIsomorphic(s string, t string) bool {
	charCount := len(s)
	if charCount < 2 {
		return true
	}
	prevSchar := s[0]
	prevTchar := t[0]
	sflags := 1
	tflags := 1

	s2tMap := make(map[byte]byte)
	s2tMap[prevSchar] = prevTchar

	for i := 1; i < charCount; i++ {
		sch := s[i]
		tch := t[i]

		if sch == prevSchar {
			sflags++
		}
		if tch == prevTchar {
			tflags++
		}

		if sflags != tflags {
			return false
		}

		mapedTch, ok := s2tMap[sch]
		if ok {
			if mapedTch != tch {
				return false
			}
		} else {
			s2tMap[sch] = tch
		}

		prevSchar = sch
		prevTchar = tch
	}
	return true
}

func main() {
	fmt.Println("true -> ", isIsomorphic("egg", "add"))
	fmt.Println("false -> ", isIsomorphic("foo", "bar"))
	fmt.Println("true -> ", isIsomorphic("paper", "title"))
}
