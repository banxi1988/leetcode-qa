package leetcode

import "testing"
import "github.com/stretchr/testify/assert"

func Test_longestIncreasingSubsequence(t *testing.T) {

	assert.Equal(t, 4, longestIncreasingSubsequence([]int{5, 3, 4, 8, 6, 7}))
}
