package main 

import "fmt"

type ListNode struct{
	Val int
	Next *ListNode
}

func dumpListNode(lnode  *ListNode){
	fmt.Print("ListNode[")
	for lnode != nil{
		fmt.Print(lnode.Val, ",")
		lnode = lnode.Next
	}
	fmt.Print("]\n")
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode{
	if l1 == nil{
		return l2
	}
	if l2 == nil{
		return l1
	}

	var l3 *ListNode 
	var current *ListNode
	for l1 != nil && l2 != nil{
		nextValue := 0
		if l1.Val < l2.Val{
			nextValue = l1.Val
			l1 = l1.Next
		}else{
			nextValue  = l2.Val
			l2 = l2.Next
		}
		if l3 == nil{
			l3 = &ListNode{nextValue, nil}
			current = l3
		}else{
			current.Next = &ListNode{nextValue, nil}
			current = current.Next
		}
	}
	if l1 != nil{
		current.Next = l1
	}else{
		current.Next = l2
	}
	return l3

}

func main(){
	l1 := &ListNode{1,nil}
	l1.Next = &ListNode{2,nil}
	l1.Next.Next = &ListNode{4,nil}

	l2 := &ListNode{1,nil}
	l2.Next = &ListNode{3,nil}
	l2.Next.Next = &ListNode{4,nil}
	dumpListNode(mergeTwoLists(l1, l2))
}