package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, sum int) bool {
	if root == nil {
		return false
	}
	if root.Left == nil && root.Right == nil {
		return root.Val == sum
	}
	if root.Left != nil {
		if hasPathSum(root.Left, sum-root.Val) {
			return true
		}
	}
	if root.Right != nil {
		if hasPathSum(root.Right, sum-root.Val) {
			return true
		}
	}

	return false

}

func main() {
	root1 := &TreeNode{Val: 5}
	root1.Left = &TreeNode{Val: 4}
	root1.Left.Left = &TreeNode{Val: 11}
	root1.Left.Left.Left = &TreeNode{Val: 7}
	root1.Left.Left.Right = &TreeNode{Val: 2}

	root1.Right = &TreeNode{Val: 8}
	root1.Right.Left = &TreeNode{Val: 13}
	root1.Right.Right = &TreeNode{Val: 4}
	root1.Right.Right.Right = &TreeNode{Val: 1}
	// 22, 27,26,18
	fmt.Println("true -> ", hasPathSum(root1, 22))
	fmt.Println("true -> ", hasPathSum(root1, 27))
	fmt.Println("true -> ", hasPathSum(root1, 26))
	fmt.Println("true -> ", hasPathSum(root1, 18))
	fmt.Println("false -> ", hasPathSum(root1, 5))
	fmt.Println("false -> ", hasPathSum(root1, 20))
}
