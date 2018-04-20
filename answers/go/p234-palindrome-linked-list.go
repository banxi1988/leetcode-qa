package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}
	// 1) 利用 快慢指针找出中间节点和末尾节点位置，当 fastNode 指向最后一个节点时，slowNode 指向中间的节点
	fastNode := head
	slowNode := head
	for fastNode.Next != nil {
		fastNode = fastNode.Next
		if fastNode.Next != nil {
			fastNode = fastNode.Next
			slowNode = slowNode.Next
		}
	}
	// 2) 反转后半部分链表
	for slowNode.Next != fastNode {
		tmpNode := slowNode.Next
		slowNode.Next = tmpNode.Next
		tmpNode.Next = fastNode.Next
		fastNode.Next = tmpNode
	}

	// 3) 从 开始和中间开始遍历比对
	midNode := fastNode
	headNode := head
	for midNode != nil {
		if headNode.Val != midNode.Val {
			return false
		}
		midNode = midNode.Next
		headNode = headNode.Next
	}

	return true
}

func main() {
	fmt.Println("true -> ", isPalindrome(nil))
	head := &ListNode{Val: 1}
	fmt.Println("true -> ", isPalindrome(head))
	head.Next = &ListNode{Val: 2}
	head.Next.Next = &ListNode{Val: 1}
	fmt.Println("true -> ", isPalindrome(head))

	head2 := &ListNode{Val: 1}
	head2.Next = &ListNode{Val: 1}
	fmt.Println("true -> ", isPalindrome(head2))

	head3 := &ListNode{Val: 1}
	head3.Next = &ListNode{Val: 2}
	fmt.Println("false -> ", isPalindrome(head3))

	head4 := &ListNode{Val: 1}
	head4.Next = &ListNode{Val: 2}
	head4.Next.Next = &ListNode{Val: 3}
	head4.Next.Next.Next = &ListNode{Val: 2}
	head4.Next.Next.Next.Next = &ListNode{Val: 1}
	fmt.Println("true -> ", isPalindrome(head4))

	head5 := &ListNode{Val: 1}
	head5.Next = &ListNode{Val: 2}
	head5.Next.Next = &ListNode{Val: 2}
	fmt.Println("false -> ", isPalindrome(head5))

	head6 := &ListNode{Val: 1}
	head6.Next = &ListNode{Val: 4}
	head6.Next.Next = &ListNode{Val: -1}
	head6.Next.Next.Next = &ListNode{Val: -1}
	head6.Next.Next.Next.Next = &ListNode{Val: 4}
	head6.Next.Next.Next.Next.Next = &ListNode{Val: 1}
	fmt.Println("true -> ", isPalindrome(head6))

	head7 := &ListNode{Val: 1}
	head7.Next = &ListNode{Val: 1}
	head7.Next.Next = &ListNode{Val: 2}
	head7.Next.Next.Next = &ListNode{Val: 1}
	fmt.Println("false -> ", isPalindrome(head7))
}
