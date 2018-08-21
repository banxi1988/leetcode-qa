package leetcode

import "testing"
import "github.com/stretchr/testify/assert"

func Test_search(t *testing.T) {
	got1 := search([]int{-1, 0, 3, 5, 9, 12}, 9)
	assert.Equal(t, 4, got1)
	got2 := search([]int{-1, 0, 3, 5, 9, 12}, 2)
	assert.Equal(t, -1, got2)
	assert.Equal(t, 0, search([]int{1}, 1))
	assert.Equal(t, 0, search([]int{1, 2}, 1))
	assert.Equal(t, 1, search([]int{1, 2}, 2))
	assert.Equal(t, 0, search([]int{1, 2, 3}, 1))
	assert.Equal(t, 1, search([]int{1, 2, 3}, 2))
	assert.Equal(t, 2, search([]int{1, 2, 3}, 3))
}
