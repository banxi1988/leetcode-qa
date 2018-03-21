package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	} else {
		if p.Val != q.Val {
			return false
		}
		return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
	}
}

func flipTree(root *TreeNode) {
	if root == nil {
		return
	}
	tmp := root.Left
	root.Left = root.Right
	root.Right = tmp
	flipTree(root.Left)
	flipTree(root.Right)
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	left := root.Left
	right := root.Right

	if left == nil && right == nil {
		return true
	}
	if left == nil || right == nil {
		return false
	}
	flipTree(right)
	return isSameTree(left, right)
}

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Left = &TreeNode{Val: 2}
	root1.Right = &TreeNode{Val: 2}
	root1.Left.Left = &TreeNode{Val: 3}
	root1.Left.Right = &TreeNode{Val: 4}
	root1.Left.Left.Left = &TreeNode{Val: 5}

	root1.Right.Left = &TreeNode{Val: 4}
	root1.Right.Right = &TreeNode{Val: 3}
	root1.Right.Right.Right = &TreeNode{Val: 5}
	fmt.Println("true -> ", isSymmetric(root1))
}
