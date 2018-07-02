package main

import (
	"fmt"
	"sort"
)

func sortBytes(bytes []byte) {
	less := func(i, j int) bool {
		return bytes[i] < bytes[j]
	}
	sort.Slice(bytes, less)
}

func searchBytes(bytes []byte, target byte) int {
	return sort.Search(len(bytes), func(i int) bool {
		return bytes[i] > target
	})
}

func nextGreatestLetter(letters []byte, target byte) byte {
	sortBytes(letters)
	i := searchBytes(letters, target)
	if i < len(letters) {
		return letters[i]
	} else {
		return letters[0]
	}
}

func main() {
	fmt.Println(byte('c'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'a'))
	fmt.Println(byte('f'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'c'))
	fmt.Println(byte('f'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'd'))
	fmt.Println(byte('j'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'g'))
	fmt.Println(byte('c'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'j'))
	fmt.Println(byte('c'), " -> ", nextGreatestLetter([]byte{'c', 'f', 'j'}, 'k'))
	fmt.Println(byte('c'), " -> ", nextGreatestLetter([]byte{'f', 'c', 'j'}, 'k'))
}
