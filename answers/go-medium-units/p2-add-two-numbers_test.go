package gmedium

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_addTwoNumbers(t *testing.T) {

	t1L1 := &ListNode{Val: 0}
	t1L2 := &ListNode{Val: 0}
	t1Got := addTwoNumbers(t1L1, t1L2)
	t1L3 := &ListNode{Val: 0}
	assert.Nil(t, t1Got.Next)
	assert.Equal(t, t1Got.Val, t1L3.Val)

	t2L1 := &ListNode{Val: 1}
	t2L1.Next = &ListNode{Val: 8}
	t2L2 := &ListNode{Val: 0}

	t2Got := addTwoNumbers(t2L1, t2L2)
	assert.NotNil(t, t2Got)
	assert.NotNil(t, t2Got.Next)
	assert.Equal(t, 1, t2Got.Val)
	assert.Equal(t, 8, t2Got.Next.Val)

	t3L1 := sliceToListNode([]int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1})
	t3L2 := sliceToListNode([]int{5, 6, 4})
	t3Got := addTwoNumbers(t3L1, t3L2)
	t3GotSlice := listNodeToSlice(t3Got)
	t3Want := []int{6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1}
	assert.ElementsMatch(t, t3Want, t3GotSlice)
}
