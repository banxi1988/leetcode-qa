package main

import "fmt"

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
)

func min(nums ...int) int {
	minNum := MaxInt
	for _, num := range nums {
		if num < minNum {
			minNum = num
		}
	}
	return minNum
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

func maxValue(branch *TreeNode) int {
	maxValue := branch.Val
	for branch != nil {
		maxValue = branch.Val
		branch = branch.Right
	}
	return maxValue
}

func minValue(branch *TreeNode) int {
	minValue := branch.Val
	for branch != nil {
		minValue = branch.Val
		branch = branch.Left
	}
	return minValue
}

func getMinimumDifference(root *TreeNode) int {
	rootLeftDiff := MaxInt
	rootRightDiff := MaxInt
	leftBranchDiff := MaxInt
	rightBranchDiff := MaxInt
	if root.Left != nil {
		rootLeftDiff = abs(root.Val - maxValue(root.Left))
		leftBranchDiff = getMinimumDifference(root.Left)
	}
	if root.Right != nil {
		rootRightDiff = abs(root.Val - minValue(root.Right))
		rightBranchDiff = getMinimumDifference(root.Right)
	}
	return min(rootLeftDiff, rootRightDiff, leftBranchDiff, rightBranchDiff)

}

func main() {
	root := &TreeNode{Val: 1}
	root.Right = &TreeNode{Val: 3}
	root.Right.Left = &TreeNode{Val: 2}

	levelOrderDump(root)

	fmt.Println("1 -> ", getMinimumDifference(root))

	root2 := &TreeNode{Val: 236}
	root2.Left = &TreeNode{Val: 104}
	root2.Right = &TreeNode{Val: 701}
	root2.Left.Right = &TreeNode{Val: 227}
	root2.Right.Right = &TreeNode{Val: 911}
	fmt.Println("9 -> ", getMinimumDifference(root2))

}
