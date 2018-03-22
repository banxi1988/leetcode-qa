package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrderBottom(root *TreeNode) [][]int {
	arrarr := [][]int{}
	if root == nil {
		return arrarr
	}
	branches := []*TreeNode{root}
	nodeDepthMap := make(map[*TreeNode]int)
	nodeDepthMap[root] = 0

	for len(branches) > 0 {
		branch := branches[0]
		branchDepth := nodeDepthMap[branch]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
			nodeDepthMap[branch.Left] = branchDepth + 1
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
			nodeDepthMap[branch.Right] = branchDepth + 1
		}
		branches = branches[1:]
		if len(arrarr) > branchDepth {
			arrarr[branchDepth] = append(arrarr[branchDepth], branch.Val)
		} else {
			arrarr = append(arrarr, []int{branch.Val})
		}
	}
	// reverse
	for i, j := 0, len(arrarr)-1; i < j; i, j = i+1, j-1 {
		tmp := arrarr[i]
		arrarr[i] = arrarr[j]
		arrarr[j] = tmp
	}

	return arrarr

}

func main() {
	root1 := &TreeNode{Val: 3}
	root1.Left = &TreeNode{Val: 9}
	root1.Left.Left = &TreeNode{Val: 11}

	root1.Right = &TreeNode{Val: 20}
	root1.Right.Left = &TreeNode{Val: 15}
	root1.Right.Right = &TreeNode{Val: 7}
	fmt.Println(levelOrderBottom(root1))
}
