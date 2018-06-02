package main

import (
	"fmt"
	"strconv"
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

func tree2str(t *TreeNode) string {
	if t == nil {
		return ""
	}
	tVal := strconv.Itoa(t.Val)
	if t.Left == nil && t.Right == nil {
		return tVal
	} else {
		leftStr := tree2str(t.Left)
		rightStr := tree2str(t.Right)
		if t.Left != nil && t.Right != nil {
			return tVal + "(" + leftStr + ")(" + rightStr + ")"
		} else if t.Right == nil {
			return tVal + "(" + leftStr + ")"
		} else {
			return tVal + "()(" + rightStr + ")"
		}
	}
}

func main() {
	fmt.Println(" -> ", tree2str(nil))
	root01 := &TreeNode{Val: 1}
	fmt.Println("1 -> ", tree2str(root01))
	root02 := &TreeNode{Val: 1}
	root02.Left = &TreeNode{Val: 2}
	fmt.Println("1(2) -> ", tree2str(root02))

	root03 := &TreeNode{Val: 1}
	root03.Right = &TreeNode{Val: 2}
	fmt.Println("1()(2) -> ", tree2str(root03))

	root := &TreeNode{Val: 1}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 3}
	root.Left.Left = &TreeNode{Val: 4}
	fmt.Println("1(2(4))(3) ->", tree2str(root))

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 2}
	root2.Right = &TreeNode{Val: 3}
	root2.Left.Right = &TreeNode{Val: 4}
	fmt.Println("1(2()(4))(3) ->", tree2str(root2))
}
