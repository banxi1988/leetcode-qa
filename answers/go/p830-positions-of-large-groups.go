package main

import "fmt"

func largeGroupPositions(S string) [][]int {
	chars := []byte(S)
	slen := len(chars)
	results := [][]int{}
	var prevChar byte
	for i := 0; i < slen-2; {
		prevChar = chars[i]
		rangeStart := i
		rangeEnd := i + 1
		for rangeEnd < slen {
			if chars[rangeEnd] == prevChar {
				rangeEnd++
				continue
			} else {
				rangeEnd--
				break
			}
		}
		if rangeEnd == slen {
			rangeEnd--
		}
		rangeLen := rangeEnd - rangeStart + 1
		i = rangeEnd + 1
		// fmt.Println(prevChar, rangeStart, rangeEnd, rangeLen)
		if rangeLen >= 3 {
			results = append(results, []int{rangeStart, rangeEnd})
		}
	}
	return results
}

func main() {
	fmt.Println("[[3,6]]  ->", largeGroupPositions("abbxxxxzzy"))
	fmt.Println("[]  ->", largeGroupPositions("abc"))
	fmt.Println("[[3,5]]  ->", largeGroupPositions("abcddd"))
	fmt.Println("[[0,2]]  ->", largeGroupPositions("aaa"))
	fmt.Println(" [[3,5],[6,9],[12,14]]  ->", largeGroupPositions("abcdddeeeeaabbbcd"))
}
