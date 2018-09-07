package leetcode



func lengthOf(head *ListNode) int {
	p := head
	count := 0
	for p != nil {
		count++
		p = p.Next
	}
	return count
}
func middleNode(head *ListNode) *ListNode {
	count := lengthOf(head)
	if count < 2 {
		return head
	}
	mid := count / 2
	p := head
	for mid > 0 {
		p = p.Next
		mid--
	}
	return p
}
