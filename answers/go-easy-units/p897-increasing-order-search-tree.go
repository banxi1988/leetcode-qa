package geasy

import (
	"sort"
)

func treeToSlice(root *TreeNode) []int {
	slice := []int{}
	if root == nil {
		return slice
	}
	levelStacks := []*TreeNode{root}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		slice = append(slice, branch.Val)
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
	}
	return slice
}

func indexOf(slice []int, x int) int {
	for i, num := range slice {
		if num == x {
			return i
		}
	}
	return -1
}

func increasingBST(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	slice := treeToSlice(root)
	sort.Ints(slice)

	leftMostValue := root.Val
	leftMost := root.Left
	for leftMost != nil {
		leftMostValue = leftMost.Val
		leftMost = leftMost.Left
	}

	newRoot := &TreeNode{Val: leftMostValue}
	rootValueIndex := indexOf(slice, leftMostValue)
	cur := newRoot
	for i := 0; i < len(slice); i++ {
		if i == rootValueIndex {
			continue
		}
		cur.Right = &TreeNode{Val: slice[i]}
		cur = cur.Right
	}
	return newRoot
}
