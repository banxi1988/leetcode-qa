package gmedium

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func includes(arr []string, s string) bool {
	for _, as := range arr {
		if as == s {
			return true
		}
	}
	return false
}

func diffStringSlices(s1, s2 []string) {
	if len(s1) < len(s2) {
		diffStringSlices(s2, s1)
		return
	}
	for _, s := range s1 {
		if !includes(s2, s) {
			println(s, " was not in s2")
		}
	}
}

func Test_generateParenthesis(t *testing.T) {
	want1 := []string{"((()))", "(()())", "(())()", "()(())", "()()()"}
	got1 := generateParenthesis(3)
	assert.ElementsMatch(t, want1, got1)

	want2 := []string{"(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"}
	got2 := generateParenthesis(4)
	println("got2 len:", len(got2))
	diffStringSlices(want2, got2)
	assert.ElementsMatch(t, want2, got2)
}
