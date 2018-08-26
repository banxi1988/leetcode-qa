package ghard

import "testing"
import "github.com/stretchr/testify/assert"

func TestFreqStack(t *testing.T) {
	stack := Constructor()
	stack.Push(5)
	stack.Push(7)
	stack.Push(5)
	stack.Push(7)
	stack.Push(4)
	stack.Push(5)
	assert.Equal(t, 5, stack.Pop())
	assert.Equal(t, 7, stack.Pop())
	assert.Equal(t, 5, stack.Pop())
	assert.Equal(t, 4, stack.Pop())
	assert.Equal(t, 7, stack.Pop())
	assert.Equal(t, 5, stack.Pop())
}
