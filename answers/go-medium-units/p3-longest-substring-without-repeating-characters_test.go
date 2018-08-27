package gmedium

import "testing"
import "github.com/stretchr/testify/assert"

func Test_lengthOfLongestSubstring(t *testing.T) {
	assert.Equal(t, 3, lengthOfLongestSubstring("abcabcbb"))
	assert.Equal(t, 1, lengthOfLongestSubstring("bbbbb"))
	assert.Equal(t, 3, lengthOfLongestSubstring("pwwkew"))
	assert.Equal(t, 2, lengthOfLongestSubstring("bbbbbc"))
	assert.Equal(t, 1, lengthOfLongestSubstring(" "))

}
