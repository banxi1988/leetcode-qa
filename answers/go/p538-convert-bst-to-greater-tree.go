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

func convertBSTInner(root *TreeNode, upstreamSum int) *TreeNode {
	if root == nil {
		return nil
	}
	// fmt.Println("branch:", root.Val, " rightSum:", rightSum)
	rightBranchSum := treeSum(root.Right)
	if root.Right != nil {
		root.Right = convertBSTInner(root.Right, upstreamSum)
	}
	root.Val = root.Val + rightBranchSum + upstreamSum
	if root.Left != nil {
		root.Left = convertBSTInner(root.Left, root.Val)
	}

	return root
}

func convertBST(root *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	// is Leaf
	if root.Left == nil && root.Right == nil {
		return root
	}
	return convertBSTInner(root, 0)
}

func main() {
	root := &TreeNode{Val: 2}
	root.Left = &TreeNode{Val: 0}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: -4}
	root.Left.Right = &TreeNode{Val: 1}
	res1 := convertBST(root)
	fmt.Println("expected: 5,6,3,2,6")
	levelOrderDump(res1)

	root2 := &TreeNode{Val: 5}
	root2.Left = &TreeNode{Val: 2}
	root2.Right = &TreeNode{Val: 13}
	res2 := convertBST(root2)
	fmt.Println("expected: 18,20,13")
	levelOrderDump(res2)

	root3 := &TreeNode{Val: 1}
	root3.Left = &TreeNode{Val: 0}
	root3.Right = &TreeNode{Val: 4}

	root3.Left.Left = &TreeNode{Val: -2}
	root3.Right.Left = &TreeNode{Val: 3}
	res3 := convertBST(root3)
	fmt.Println("expected: 8,8,4,6,7")
	levelOrderDump(res3)

}
