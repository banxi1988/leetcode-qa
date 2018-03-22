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

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Left = &TreeNode{Val: 2}
	root1.Right = &TreeNode{Val: 2}
	root1.Left.Left = &TreeNode{Val: 3}
	root1.Left.Right = &TreeNode{Val: 4}
	root1.Left.Left.Left = &TreeNode{Val: 5}
	fmt.Println("4 -> ", maxDepth(root1))
}
