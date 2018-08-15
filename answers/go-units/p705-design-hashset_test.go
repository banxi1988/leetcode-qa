package leetcode

import "testing"
import "github.com/stretchr/testify/assert"

func TestMyHashSet_Contains(t *testing.T) {
	set := Constructor()
	set.Add(1)
	set.Add(2)
	assert.True(t, set.Contains(1))
	assert.True(t, set.Contains(2))
	assert.False(t, set.Contains(3))
	set.Add(2)
	assert.True(t, set.Contains(2))
	set.Remove(2)
	assert.False(t, set.Contains(2))
}
