Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


首先是一个 O(n) + O(n) 的解法：
主要是有一个将 ListNode 转成数组的过程需要 O(n) 的空间。

```go
func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}
	curNode := head
	nums := []int{}
	for curNode != nil {
		nums = append(nums, curNode.Val)
		curNode = curNode.Next
	}
	numCount := len(nums)
	for i, j := 0, numCount-1; i < j; i, j = i+1, j-1 {
		if nums[i] != nums[j] {
			return false
		}
	}
	return true
}
```

要实现一个 O(n) + O(1) 的解法，就不能使用数组。
但是可以利用上面的思想。
1） 先得到链表的长度这里时间是  N.
2) 比较 第 i 项，然后向前走 （n- i） 步与 第 (n - i) 项比较。
3） 重复 2，直到 i >= (n -i)
这里的总时间成本是： n + (n-1) + (n -2) + ... + 2 + 1 = n(n+1)/2 ~= O(n2)

所以这样的算法也是满足 O(n) 的优化要求的。

利用回文数的特点来计算。
比如 1,3,5,3,1, 这样符合回文的链接 要求 1 + 2 = 2 + 1. 所以，
我们可以先得到链接的长度。然后一个指针从 head 开始，另一个指针中间对称点开始向前开始。
如果他们的和与前一次指针处的各相同，那就认为是符合回文规则的。

有的情况就要复杂一些了。比如 1,2,5,7,5,2,1。 这样。
1 + 5 就不等于 2 + 2. 所以上面的算法只能识别部分回文。
