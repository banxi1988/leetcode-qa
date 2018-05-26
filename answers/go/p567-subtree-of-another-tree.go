package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderTreeString(root *TreeNode) string {
	if root == nil {
		return ""
	}
	strs := []string{}
	levelStacks := []*TreeNode{root}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		if branch == nil {
			strs = append(strs, "nil")
			continue
		} else {
			strs = append(strs, strconv.Itoa(branch.Val))
			levelStacks = append(levelStacks, branch.Left)
			levelStacks = append(levelStacks, branch.Right)
		}
	}
	return strings.Join(strs, ",")
}

func isSubtree(s *TreeNode, t *TreeNode) bool {
	if s == nil && t == nil {
		return true
	}
	if s == nil {
		return false
	}
	if t == nil {
		return true
	}
	tstr := levelOrderTreeString(t)
	branches := []*TreeNode{s}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		branchStr := levelOrderTreeString(branch)
		if branchStr == tstr {
			return true
		}
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}

		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
	}
	return false
}

func main() {
	s1 := &TreeNode{Val: 3}
	s1.Left = &TreeNode{Val: 4}
	s1.Right = &TreeNode{Val: 5}
	s1.Left.Left = &TreeNode{Val: 1}
	s1.Left.Right = &TreeNode{Val: 2}

	t := &TreeNode{Val: 4}
	t.Left = &TreeNode{Val: 1}
	t.Right = &TreeNode{Val: 2}

	s2 := &TreeNode{Val: 3}
	s2.Left = &TreeNode{Val: 4}
	s2.Right = &TreeNode{Val: 5}
	s2.Left.Left = &TreeNode{Val: 1}
	s2.Left.Right = &TreeNode{Val: 2}
	s2.Left.Right.Left = &TreeNode{Val: 0}

	fmt.Println("true -> ", isSubtree(s1, t))
	fmt.Println("false -> ", isSubtree(s2, t))

}
