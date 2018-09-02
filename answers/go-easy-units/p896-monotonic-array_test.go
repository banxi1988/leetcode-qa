package geasy

import "testing"
import "github.com/stretchr/testify/assert"

func Test_isMonotonic(t *testing.T) {
	assert.True(t, isMonotonic([]int{1, 2, 2, 3}))
	assert.True(t, isMonotonic([]int{6, 5, 4, 4}))
	assert.False(t, isMonotonic([]int{1, 3, 2}))
	assert.True(t, isMonotonic([]int{1, 2, 4, 5}))
	assert.True(t, isMonotonic([]int{1, 1, 1}))
}
