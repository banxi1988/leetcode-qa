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

const (
	MaxInt = int(^uint(0) >> 1)
	MinInt = -MaxInt - 1
)

func minValueInBST(root *TreeNode) int {
	if root.Left != nil {
		return minValueInBST(root.Left)
	} else {
		return root.Val
	}
}

func maxValueInBST(root *TreeNode) int {
	if root.Right != nil {
		return maxValueInBST(root.Right)
	} else {
		return root.Val
	}
}

func minDiffInBST(root *TreeNode) int {
	minDiff := MaxInt
	if root == nil {
		return minDiff
	}
	if root.Left != nil {
		leftMaxValue := maxValueInBST(root.Left)
		diff := root.Val - leftMaxValue
		if diff < minDiff {
			minDiff = diff
		}
		leftDiff := minDiffInBST(root.Left)
		if leftDiff < minDiff {
			minDiff = leftDiff
		}
	}
	if root.Right != nil {
		rightMinValue := minValueInBST(root.Right)
		diff := rightMinValue - root.Val
		if diff < minDiff {
			minDiff = diff
		}
		rightDiff := minDiffInBST(root.Right)
		if rightDiff < minDiff {
			minDiff = rightDiff
		}
	}
	return minDiff
}

func main() {
	root := &TreeNode{Val: 4}
	root.Left = &TreeNode{Val: 2}
	root.Left.Left = &TreeNode{Val: 1}
	root.Left.Right = &TreeNode{Val: 3}
	root.Right = &TreeNode{Val: 6}

	fmt.Println("1 -> ", minDiffInBST(root))

	root2 := &TreeNode{Val: 27}
	root2.Right = &TreeNode{Val: 34}
	root2.Right.Right = &TreeNode{Val: 58}
	root2.Right.Right.Left = &TreeNode{Val: 50}
	root2.Right.Right.Left.Left = &TreeNode{Val: 44}

	fmt.Println("6 -> ", minDiffInBST(root2))

	root3 := &TreeNode{Val: 90}
	root3.Left = &TreeNode{Val: 69}
	root3.Left.Left = &TreeNode{Val: 49}
	root3.Left.Right = &TreeNode{Val: 89}
	root3.Left.Left.Right = &TreeNode{Val: 52}

	fmt.Println("1 -> ", minDiffInBST(root3))
}
