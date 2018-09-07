package main

import (
	"bytes"
	"fmt"
)

func numJewelsInStones(J string, S string) int {
	jbytes := []byte(J)
	sbytes := []byte(S)

	count := 0
	for _, s := range sbytes {
		if bytes.IndexByte(jbytes, s) != -1 {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println("3 ->", numJewelsInStones("aA", "aAAbb"))
	fmt.Println("0 ->", numJewelsInStones("z", "ZZ"))
}
