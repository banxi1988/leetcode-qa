Reverse a singly linked list.


Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

首先是一种递归的写法：

核心思想是，取第一个节点， 然后就可以递归反转其他节点返回新的头。然后将第一个节点接到最后面。

```go
func reverseList(head *ListNode) *ListNode {
	// recursive
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return head
	}

	newHead := reverseList(head.Next)
	lastNode := newHead
	for lastNode.Next != nil {
		lastNode = lastNode.Next
	}
	lastNode.Next = head
	head.Next = nil
	return newHead
}
```

迭代解法。如果是数组或者双向链接，可以通过两头向中间遍历然后交换前后循环节点值来实现。
但是这个是单向链接所以得想其他办法。

首先是一个一个数字，一个数字移到的代码.

```go
p1 := head
	p2 := head.Next
	for p2 != nil {
		tmpVal := p1.Val
		p1.Val = p2.Val
		p2.Val = tmpVal

		p1 = p2
		p2 = p2.Next
	}
	return head
```
这样可以将链表 1,2,3,4,5 转成  2,3,4,5, 1。即反转了一个数过去。
如果下一次将 2 转过去，这个不停循环就可以了。

于是得到下面的迭代版本：

```go
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
```
