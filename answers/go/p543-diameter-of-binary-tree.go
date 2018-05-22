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

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	ld := 0
	rd := 0
	if root.Left != nil {
		ld = maxDepth(root.Left) + 1
	}
	if root.Right != nil {
		rd = maxDepth(root.Right) + 1
	}
	if ld > rd {
		return ld
	}
	return rd
}

func diameterOfBranch(root *TreeNode) int {
	ld := 0
	rd := 0
	if root == nil {
		return 0
	}
	if root.Left != nil {
		ld = maxDepth(root.Left) + 1
	}
	if root.Right != nil {
		rd = maxDepth(root.Right) + 1
	}
	return ld + rd
}

func diameterOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	levelStacks := []*TreeNode{root}
	maxLen := 0
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		branchLen := diameterOfBranch(branch)
		if branchLen > maxLen {
			maxLen = branchLen
		}
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
	}
	return maxLen
}

func main() {
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: 4}
	root.Left.Right = &TreeNode{Val: 5}
	levelOrderDump(root)
	fmt.Println("3 ->", diameterOfBinaryTree(root))

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 2}
	root2.Right = &TreeNode{Val: 3}
	root2.Left.Left = &TreeNode{Val: 4}
	root2.Left.Right = &TreeNode{Val: 5}

	root2.Left.Left.Left = &TreeNode{Val: 6}
	root2.Left.Right.Right = &TreeNode{Val: 7}

	root2.Left.Left.Left.Left = &TreeNode{Val: 8}
	root2.Left.Right.Right.Right = &TreeNode{Val: 9}
	fmt.Println("6 ->", diameterOfBinaryTree(root2))
}
