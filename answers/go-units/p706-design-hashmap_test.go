package leetcode

import "testing"
import "github.com/stretchr/testify/assert"

func TestMyHashMap_Contains(t *testing.T) {
	hm := ConstructorHashMap()
	hm.Put(1, 1)
	hm.Put(2, 2)
	assert.Equal(t, 1, hm.Get(1))
	assert.Equal(t, 2, hm.Get(2))
	assert.Equal(t, -1, hm.Get(3))
	hm.Put(2, 1)
	assert.Equal(t, 1, hm.Get(2))
	hm.Remove(2)
	assert.Equal(t, -1, hm.Get(2))
}
