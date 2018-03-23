package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftMax := maxDepth(root.Left)
	rightMax := maxDepth(root.Right)
	if leftMax > rightMax {
		return leftMax + 1
	}
	return rightMax + 1
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	diff := leftDepth - rightDepth
	isCurrentNodeBalance := (diff >= 0 && diff < 2) || (diff < 0 && diff > -2)
	if !isCurrentNodeBalance {
		return false
	}
	return isBalanced(root.Left) && isBalanced(root.Right)
}

func main() {
	root1 := &TreeNode{Val: 3}
	root1.Left = &TreeNode{Val: 9}
	root1.Right = &TreeNode{Val: 20}
	root1.Right.Left = &TreeNode{Val: 15}
	root1.Right.Right = &TreeNode{Val: 7}
	fmt.Println("true -> ", isBalanced(root1))
}
