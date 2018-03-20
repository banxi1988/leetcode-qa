package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dumpTree(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Print(root.Val, ", ")
	left := root.Left
	right := root.Right
	if left != nil {
		dumpTree(left)
	}
	if right != nil {
		dumpTree(right)
	}
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

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Left = &TreeNode{Val: 2}
	root1.Right = &TreeNode{Val: 3}

	root12 := &TreeNode{Val: 1}
	root12.Left = &TreeNode{Val: 2}
	root12.Right = &TreeNode{Val: 3}

	fmt.Println(" true -> ", isSameTree(root1, root12))

}
