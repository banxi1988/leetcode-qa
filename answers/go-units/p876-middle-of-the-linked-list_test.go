package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func listNodeToSlice(head *ListNode) []int {
	slice := []int{}
	p := head
	for p != nil {
		slice = append(slice, p.Val)
		p = p.Next
	}
	return slice
}

func sliceToListNode(slice []int) *ListNode {
	if len(slice) == 0 {
		return nil
	}
	head := &ListNode{Val: slice[0]}
	p := head
	for i := 1; i < len(slice); i++ {
		p.Next = &ListNode{Val: slice[i]}
		p = p.Next
	}
	return head
}

func Test_middleNode(t *testing.T) {
	type args struct {
		head *ListNode
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"e1", args{sliceToListNode([]int{1, 2, 3, 4, 5})}, []int{3, 4, 5}},
		{"e2", args{sliceToListNode([]int{1, 2, 3, 4, 5, 6})}, []int{4, 5, 6}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			node := middleNode(tt.args.head)
			got := listNodeToSlice(node)
			assert.ElementsMatch(t, got, tt.want)
		})
	}
}
