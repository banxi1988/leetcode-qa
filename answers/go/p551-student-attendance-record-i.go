package main

import (
	"fmt"
)

func checkRecord(s string) bool {
	letters := []byte(s)
	absentCount := 0
	lateCount := 0
	for i := 0; i < len(letters); i++ {
		letter := letters[i]
		switch letter {
		case 'A':
			absentCount++
			if absentCount > 1 {
				return false
			}
			lateCount = 0
		case 'L':
			lateCount++
			if lateCount > 2 {
				return false
			}
		default:
			lateCount = 0
		}
	}
	return true
}

func main() {
	fmt.Println("True ->", checkRecord("PPALLP"))
	fmt.Println("False ->", checkRecord("PPALLL"))
}
