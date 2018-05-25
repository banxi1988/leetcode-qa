package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func treeSum(root *TreeNode) int {
	if root == nil {
		return 0
	}
	levelStacks := []*TreeNode{root}
	sum := 0
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		sum += branch.Val
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
	}
	return sum
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func findTilt(root *TreeNode) int {
	if root == nil {
		return 0
	}

	levelStacks := []*TreeNode{root}
	treeTilt := 0
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}

		leftTreeSum := treeSum(left)
		rightTreeSum := treeSum(right)
		// fmt.Println("branch: ", branch.Val, " leftTreeSum: ", leftTreeSum, " rightTreeSum:", rightTreeSum)
		tilt := abs(leftTreeSum - rightTreeSum)
		treeTilt += tilt
	}
	return treeTilt
}

func main() {
	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}

	fmt.Println("1 -> ", findTilt(root))
}
