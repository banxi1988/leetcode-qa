package gmedium

import (
	"strconv"
)

func combLetters(letters []string) []string {
	lettersCount := len(letters)
	if lettersCount < 1 {
		return []string{}
	} else if lettersCount < 2 {
		result := []string{}
		for _, letter := range letters[0] {
			result = append(result, string(letter))
		}
		return result
	}
	keys := letters[0]
	remainResults := combLetters(letters[1:])
	result := []string{}
	for _, key := range keys {
		keyStr := string(key)
		for _, result2 := range remainResults {
			result = append(result, keyStr+result2)
		}
	}
	return result

}

func letterCombinations(digits string) []string {
	numLetters := []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
	letters := []string{}
	for _, digit := range []byte(digits) {
		num, _ := strconv.Atoi(string(digit))
		letters = append(letters, numLetters[num])
	}
	return combLetters(letters)
}
