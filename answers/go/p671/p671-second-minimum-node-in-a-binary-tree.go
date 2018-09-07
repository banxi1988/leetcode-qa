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

func btreeFromLevelOrder(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	root := &TreeNode{Val: nums[0]}
	remainNums := nums[1:]
	levelStacks := []*TreeNode{root}
	for len(remainNums) > 1 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		if remainNums[0] != -1 {
			left := &TreeNode{Val: remainNums[0]}
			branch.Left = left
			levelStacks = append(levelStacks, left)
		}
		if remainNums[1] != -1 {
			right := &TreeNode{Val: remainNums[1]}
			branch.Right = right
			remainNums = remainNums[2:]
			levelStacks = append(levelStacks, right)
		}
	}
	if len(remainNums) > 0 && remainNums[0] != -1 {
		branch := levelStacks[0]
		branch.Left = &TreeNode{Val: remainNums[0]}
	}
	return root
}

func mini(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func findSecondMinimumValue(root *TreeNode) int {
	if root == nil {
		return -1
	}
	rootVal := root.Val
	if root.Left == nil && root.Right == nil {
		return -1
	}
	if root.Left != nil && root.Right != nil {
		leftVal := root.Left.Val
		rightVal := root.Right.Val
		if leftVal > rootVal && rightVal > rootVal {
			return mini(leftVal, rightVal)
		}
		// all equal
		lsValue := findSecondMinimumValue(root.Left)
		rsValue := findSecondMinimumValue(root.Right)
		if lsValue != -1 && rsValue != -1 {
			return mini(lsValue, rsValue)
		}
		if lsValue != -1 {
			return lsValue
		}
		return rsValue // -1 or not, all ok
	}

	if root.Left != nil {
		leftVal := root.Left.Val
		if rootVal < leftVal {
			return leftVal
		}
		return findSecondMinimumValue(root.Left)
	}

	rightVal := root.Right.Val
	if rootVal < rightVal {
		return rightVal
	}
	return findSecondMinimumValue(root.Right)
}

func main() {
	root := &TreeNode{Val: 2}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 5}
	root.Right.Left = &TreeNode{Val: 5}
	root.Right.Right = &TreeNode{Val: 7}

	// fmt.Println("5 -> ", findSecondMinimumValue(root))

	root2 := &TreeNode{Val: 2}
	root2.Left = &TreeNode{Val: 2}
	root2.Right = &TreeNode{Val: 2}

	// fmt.Println("-1 -> ", findSecondMinimumValue(root2))

	root3 := &TreeNode{Val: 2}
	root3.Left = &TreeNode{Val: 2}
	root3.Right = &TreeNode{Val: 2}

	root3.Left.Left = &TreeNode{Val: 3}
	// fmt.Println("3 -> ", findSecondMinimumValue(root3))

	root4 := btreeFromLevelOrder([]int{1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1})
	levelOrderDump(root4)
	fmt.Println("2 -> ", findSecondMinimumValue(root4))

}
