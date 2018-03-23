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

	return arrarr

}

func sortedArrayToBST(nums []int) *TreeNode {
	numCount := len(nums)
	switch numCount {
	case 0:
		return nil
	case 1:
		return &TreeNode{Val: nums[0]}
	case 2:
		branch := &TreeNode{Val: nums[0]}
		branch.Right = &TreeNode{Val: nums[1]}
		return branch
	default:
		mid := numCount / 2
		branch := &TreeNode{Val: nums[mid]}
		branch.Left = sortedArrayToBST(nums[:mid])
		branch.Right = sortedArrayToBST(nums[mid+1:])
		return branch
	}
}

func main() {
	arr := []int{1, 2, 3}
	fmt.Println(arr[:1], arr[1:])
	fmt.Println(levelOrderBottom(sortedArrayToBST([]int{-10, -3, 0, 5, 9})))
}
