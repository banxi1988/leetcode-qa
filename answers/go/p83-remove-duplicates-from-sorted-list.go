package main

import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func dumpListNode(lnode *ListNode) {
	fmt.Print("ListNode[")
	for lnode != nil {
		fmt.Print(lnode.Val, ",")
		lnode = lnode.Next
	}
	fmt.Print("]\n")
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	prevVal := head.Val
	currentNode := head.Next
	linkNode := head
	for currentNode != nil {
		if currentNode.Val == prevVal {
			linkNode.Next = currentNode.Next
		} else {
			linkNode = linkNode.Next
		}
		prevVal = currentNode.Val
		currentNode = currentNode.Next

	}
	return head
}

func main() {
	l1 := &ListNode{1, nil}
	l1.Next = &ListNode{1, nil}
	l1.Next.Next = &ListNode{2, nil}

	l2 := &ListNode{1, nil}
	l2.Next = &ListNode{1, nil}
	l2.Next.Next = &ListNode{2, nil}
	l2.Next.Next.Next = &ListNode{3, nil}
	l2.Next.Next.Next.Next = &ListNode{3, nil}

	l3 := &ListNode{1, nil}
	l3.Next = &ListNode{1, nil}
	l3.Next.Next = &ListNode{1, nil}

	l4 := &ListNode{1, nil}

	dumpListNode(deleteDuplicates(l1))
	dumpListNode(deleteDuplicates(l2))
	dumpListNode(deleteDuplicates(l3))
	dumpListNode(deleteDuplicates(l4))

}
