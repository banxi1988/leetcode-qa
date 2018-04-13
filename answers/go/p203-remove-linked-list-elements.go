package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	var bridge *ListNode
	var newHead *ListNode
	curNode := head
	for curNode != nil {
		if curNode.Val == val {
			if bridge != nil {
				bridge.Next = curNode.Next
			}
		} else {
			if bridge == nil {
				bridge = curNode
				newHead = curNode
			} else {
				bridge = bridge.Next
			}
		}
		curNode = curNode.Next
	}
	return newHead
}

func dumpListNode(head *ListNode) {
	curNode := head
	for curNode != nil {
		fmt.Print(curNode.Val, " -> ")
		curNode = curNode.Next
	}
	fmt.Println("nil")
}

func main() {
	head := &ListNode{Val: 1}
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 6}
	head.Next.Next.Next = &ListNode{Val: 3}
	head.Next.Next.Next.Next = &ListNode{Val: 4}
	head.Next.Next.Next.Next.Next = &ListNode{Val: 5}
	head.Next.Next.Next.Next.Next.Next = &ListNode{Val: 6}

	rHead := removeElement(head, 6)
	dumpListNode(rHead)

	head2 := &ListNode{Val: 2}
	head2.Next = &ListNode{Val: 2}
	r2Head := removeElement(head2, 2)
	dumpListNode(r2Head)

}
