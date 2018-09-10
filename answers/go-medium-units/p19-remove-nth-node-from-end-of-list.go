package gmedium

// |             |
// ->[1] -> [2] -> [3] -> [4] -> [5]-> nil
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	p1 := head
	p2 := head
	for i := 0; i < n; i++ {
		p1 = p1.Next
	}
	for p1 != nil && p1.Next != nil {
		p1 = p1.Next
		p2 = p2.Next
	}
	if p1 == nil {
		return head.Next
	}
	p2.Next = p2.Next.Next
	return head
}
