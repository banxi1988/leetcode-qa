package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}

	var endNode *ListNode
	for head != endNode {
		p1 := head
		p2 := head.Next
		for p2 != endNode && p2 != nil {
			tmpVal := p1.Val
			p1.Val = p2.Val
			p2.Val = tmpVal

			p1 = p2
			p2 = p2.Next
		}
		endNode = p1
	}
	return head
}

func dumpListNode(head *ListNode) {
	cur := head
	for cur != nil {
		fmt.Print(cur.Val)
		fmt.Print(" -> ")
		cur = cur.Next
	}
	fmt.Println("nil")
}

func main() {
	l1 := &ListNode{Val: 1}
	l1.Next = &ListNode{Val: 2}
	l1.Next.Next = &ListNode{Val: 3}
	l1.Next.Next.Next = &ListNode{Val: 4}
	l1.Next.Next.Next.Next = &ListNode{Val: 5}
	rl1 := reverseList(l1)
	fmt.Print("5 -> 4 -> 3 -> 2 -> 1 -> nil   actual:")
	dumpListNode(rl1)

	l2 := &ListNode{Val: 2}
	rl2 := reverseList(l2)
	fmt.Print("2 -> nil   actual:")
	dumpListNode(rl2)

	var l3 *ListNode
	rl3 := reverseList(l3)
	dumpListNode(rl3)
}
