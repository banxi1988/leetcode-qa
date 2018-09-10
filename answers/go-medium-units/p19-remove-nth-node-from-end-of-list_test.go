package gmedium

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_removeNthFromEnd(t *testing.T) {
	l1 := sliceToListNode([]int{1, 2, 3, 4, 5})
	l1Want := []int{1, 2, 3, 5}
	l1GotList := removeNthFromEnd(l1, 2)
	l1Got := listNodeToSlice(l1GotList)
	assert.Equal(t, l1Want, l1Got)

	l2 := sliceToListNode([]int{1, 2})
	l2Want := []int{2}
	l2GotList := removeNthFromEnd(l2, 2)
	l2Got := listNodeToSlice(l2GotList)
	assert.Equal(t, l2Want, l2Got)

	l3 := sliceToListNode([]int{1, 2, 3})
	l3Want := []int{1, 3}
	l3GotList := removeNthFromEnd(l3, 2)
	l3Got := listNodeToSlice(l3GotList)
	assert.Equal(t, l3Want, l3Got)

	l4GotList := removeNthFromEnd(&ListNode{Val: 1}, 1)
	assert.Nil(t, l4GotList)

	l5 := sliceToListNode([]int{1, 2})
	l5Want := []int{1}
	l5GotList := removeNthFromEnd(l5, 1)
	l5Got := listNodeToSlice(l5GotList)
	assert.Equal(t, l5Want, l5Got)
}
