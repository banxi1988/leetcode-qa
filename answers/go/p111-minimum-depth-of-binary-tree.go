package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if root.Left == nil && root.Right == nil {
		return 1
	}
	min := 1<<63 - 1
	branches := []*TreeNode{root}
	branchDepthMap := map[*TreeNode]int{root: 1}
	for len(branches) > 0 {
		branch := branches[0]
		branchDepth := branchDepthMap[branch]
		if branch.Left == nil && branch.Right == nil {
			if branchDepth < min {
				min = branchDepth
			}
		} else {
			if branch.Left != nil {
				branches = append(branches, branch.Left)
				branchDepthMap[branch.Left] = branchDepth + 1
			}
			if branch.Right != nil {
				branches = append(branches, branch.Right)
				branchDepthMap[branch.Right] = branchDepth + 1
			}
		}

		branches = branches[1:]
	}
	return min

}

func main() {
	root1 := &TreeNode{Val: 1}
	// root1.Right = &TreeNode{Val: 2}
	// root1.Right.Right = &TreeNode{Val: 3}
	fmt.Println(minDepth(root1))
}
