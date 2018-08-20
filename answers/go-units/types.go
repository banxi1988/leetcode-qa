package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// ListNode  单链表
type ListNode struct {
	Val  int
	Next *ListNode
}

// SliceOfTree return slice of level travel values
func SliceOfTree(root *TreeNode) []int {
	slice := []int{}
	if root == nil {
		return slice
	}
	levelStacks := []*TreeNode{root}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		slice = append(slice, branch.Val)
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
	}
	return slice
}
