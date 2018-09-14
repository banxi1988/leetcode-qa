package gmedium

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_swapPairs(t *testing.T) {
	l1 := sliceToListNode([]int{1, 2, 3, 4})
	want1 := []int{2, 1, 4, 3}
	gotl1 := swapPairs(l1)
	got1 := listNodeToSlice(gotl1)
	assert.Equal(t, want1, got1)
}
