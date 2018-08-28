package gmedium

import "testing"
import "github.com/stretchr/testify/assert"

func Test_longestPalindrome(t *testing.T) {
	assert.Equal(t, "bab", longestPalindrome("babad"))
	assert.Equal(t, "bb", longestPalindrome("cbbd"))
	assert.Equal(t, "bb", longestPalindrome("bb"))
	assert.Equal(t, "bb", longestPalindrome("cbb"))
	assert.Equal(t, "b", longestPalindrome("b"))
}
