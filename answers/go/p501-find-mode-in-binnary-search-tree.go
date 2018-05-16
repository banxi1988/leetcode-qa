package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dumpTree(root *TreeNode) {
	if root == nil {
		fmt.Println("nil")
		return
	}
	branches := []*TreeNode{root}
	fmt.Print("[")
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
		if len(branches) > 0 {
			fmt.Print(branch.Val, ",")
		} else {
			fmt.Print(branch.Val, "")
		}
	}
	fmt.Println("]")
}

func findMode(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	maxCount := 0
	nodeCountMap := make(map[int]int)
	branches := []*TreeNode{root}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
		count, _ := nodeCountMap[branch.Val]
		count++
		nodeCountMap[branch.Val] = count
		if count > maxCount {
			maxCount = count
		}
	}

	result := []int{}
	for num, count := range nodeCountMap {
		if count == maxCount {
			result = append(result, num)
		}
	}
	return result
}

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Right = &TreeNode{Val: 2}
	root1.Right.Left = &TreeNode{Val: 2}

	fmt.Println("[2] ->", findMode(root1))

	root2 := &TreeNode{Val: 3}
	fmt.Println("[3] ->", findMode(root2))
}
