package gmedium



func numsToNum(nums []int) int {
	numCount := len(nums)
	if numCount < 1 {
		return 0
	}
	num := 0
	base := 1
	for i := 0; i < numCount; i++ {
		num += (nums[i] * base)
		base *= 10
	}
	return num
}

func numToNums(num int) []int {
	if num < 1 {
		return []int{0}
	}
	nums := []int{}
	for num > 0 {
		digit := num % 10
		nums = append(nums, digit)
		num = num / 10
	}
	return nums
}

func addTwoNumbersLimited(l1 *ListNode, l2 *ListNode) *ListNode {
	nums1 := listNodeToSlice(l1)
	nums2 := listNodeToSlice(l2)
	num1 := numsToNum(nums1)
	num2 := numsToNum(nums2)

	outputNum := num1 + num2
	outputNums := numToNums(outputNum)
	return sliceToListNode(outputNums)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{Val: 0}
	cur := head
	p1 := l1
	p2 := l2
	carry := 0
	for p1 != nil || p2 != nil {
		num := carry
		if p1 != nil {
			num += p1.Val
			p1 = p1.Next
		}
		if p2 != nil {
			num += p2.Val
			p2 = p2.Next
		}
		val := num % 10
		if num >= 10 {
			carry = 1
		} else {
			carry = 0
		}
		cur.Next = &ListNode{Val: val}
		cur = cur.Next
	}
	if carry == 1 {
		cur.Next = &ListNode{Val: 1}
	}
	return head.Next
}
