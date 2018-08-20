package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_constructFromPrePost(t *testing.T) {
	gotTree := constructFromPrePost([]int{1, 2, 4, 5, 3, 6, 7}, []int{4, 5, 2, 6, 7, 3, 1})
	gotSlice1 := SliceOfTree(gotTree)
	assert.ElementsMatch(t, gotSlice1, []int{1, 2, 3, 4, 5, 6, 7})

	gotTree2 := constructFromPrePost([]int{2, 1, 3}, []int{3, 1, 2})
	gotSlice2 := SliceOfTree(gotTree2)
	assert.ElementsMatch(t, gotSlice2, []int{2, 1, 3})
}
