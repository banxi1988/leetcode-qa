package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderDump(root *TreeNode) {
	if root == nil {
		return
	}
	levelStacks := []*TreeNode{root}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		fmt.Print(branch.Val, ",")
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
	}
	fmt.Println("")
}

func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 == nil {
		return t2
	}
	if t2 == nil {
		return t1
	}
	root := t1
	root.Val = t1.Val + t2.Val
	root.Left = mergeTrees(t1.Left, t2.Left)
	root.Right = mergeTrees(t1.Right, t2.Right)
	return root
}

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Left = &TreeNode{Val: 3}
	root1.Right = &TreeNode{Val: 2}
	root1.Left.Left = &TreeNode{Val: 5}

	root2 := &TreeNode{Val: 2}
	root2.Left = &TreeNode{Val: 1}
	root2.Right = &TreeNode{Val: 3}
	root2.Left.Right = &TreeNode{Val: 4}
	root2.Right.Right = &TreeNode{Val: 7}

	result1 := mergeTrees(root1, root2)
	fmt.Println("3,4,5,5,4,7 -> ")
	levelOrderDump(result1)

}
