package main

// 15 May 2018

import (
	"fmt"
	"strings"
)

func findWords(words []string) []string {
	rows := []string{"qwertyuiop", "asdfghjkl", "zxcvbnm"}
	letterRowIndexMap := make(map[byte]int, 26)
	for rowIndex := 0; rowIndex < len(rows); rowIndex++ {
		row := rows[rowIndex]
		for _, letter := range []byte(row) {
			letterRowIndexMap[letter] = rowIndex
		}
	}

	results := []string{}
	for wordIndex := 0; wordIndex < len(words); wordIndex++ {
		word := strings.ToLower(words[wordIndex])
		rowIndex, _ := letterRowIndexMap[word[0]]
		allInOneRow := true
		for _, letter := range []byte(word) {
			index, _ := letterRowIndexMap[letter]
			if index != rowIndex {
				allInOneRow = false
				break
			}
		}
		if allInOneRow {
			results = append(results, words[wordIndex])
		}
	}
	return results

}
func main() {
	arr1 := []string{"Hello", "Alaska", "Dad", "Peace"}
	fmt.Println("Alaska, Dad -> ", findWords(arr1))
}
