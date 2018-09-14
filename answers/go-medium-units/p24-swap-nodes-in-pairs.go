package gmedium

///  pH    H|C   N
/// [] -> [1] -> [2] -> [3] -> [4] -> nil
func swapPairs(head *ListNode) *ListNode {
	prehead := &ListNode{Val: -1, Next: head}
	pre := prehead
	cur := head
	for cur != nil && cur.Next != nil {
		nextCur := cur.Next.Next
		next := cur.Next
		pre.Next = next
		next.Next = cur
		cur.Next = nextCur

		pre = cur
		cur = nextCur
		// slice := listNodeToSlice(prehead.Next)
		// println("current List:", slice)
	}
	return prehead.Next
}
