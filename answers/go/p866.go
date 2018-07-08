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

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
	levelStacks := []*TreeNode{root}
	branchLevelMap := make(map[*TreeNode]int)
	nodeParentMap := make(map[*TreeNode]*TreeNode)
	branchLevelMap[root] = 1
	maxLevel := 1
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		level, _ := branchLevelMap[branch]
		nextLevel := level + 1
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
			branchLevelMap[left] = nextLevel
			nodeParentMap[left] = branch
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
			branchLevelMap[right] = nextLevel
			nodeParentMap[right] = branch
		}
		if level > maxLevel {
			maxLevel = level
		}

	}

	maxLevelNodes := []*TreeNode{}
	for branch, level := range branchLevelMap {
		if level == maxLevel {
			maxLevelNodes = append(maxLevelNodes, branch)
		}
	}

	for len(maxLevelNodes) > 1 {
		parentNodeSetMap := make(map[*TreeNode]bool)
		for _, node := range maxLevelNodes {
			parentNode := nodeParentMap[node]
			parentNodeSetMap[parentNode] = true
		}
		maxLevelNodes = []*TreeNode{}
		for node := range parentNodeSetMap {
			maxLevelNodes = append(maxLevelNodes, node)
		}
	}
	return maxLevelNodes[0]
}

func main() {
	root := &TreeNode{Val: 3}
	root.Left = &TreeNode{Val: 5}
	root.Left.Left = &TreeNode{Val: 6}
	root.Left.Right = &TreeNode{Val: 2}
	root.Left.Right.Left = &TreeNode{Val: 7}
	root.Left.Right.Right = &TreeNode{Val: 4}
	root.Right = &TreeNode{Val: 1}
	root.Right.Left = &TreeNode{Val: 0}
	root.Right.Right = &TreeNode{Val: 8}

	result1 := subtreeWithAllDeepest(root)
	fmt.Println("2,7,4 -> ")
	levelOrderDump(result1)

	root2 := &TreeNode{Val: 1}
	result2 := subtreeWithAllDeepest(root2)
	fmt.Println("1 -> ")
	levelOrderDump(result2)

	root3 := &TreeNode{Val: 0}
	root3.Left = &TreeNode{Val: 1}
	root3.Right = &TreeNode{Val: 3}
	root3.Left.Right = &TreeNode{Val: 2}

	result3 := subtreeWithAllDeepest(root3)
	fmt.Println("2 -> ")
	levelOrderDump(result3)

	root4 := &TreeNode{Val: 0}
	root4.Left = &TreeNode{Val: 3}
	root4.Right = &TreeNode{Val: 1}

	root4.Left.Left = &TreeNode{Val: 4}
	root4.Left.Left.Right = &TreeNode{Val: 6}

	root4.Right.Left = &TreeNode{Val: 6}
	root4.Right.Left.Right = &TreeNode{Val: 5}

	result4 := subtreeWithAllDeepest(root4)
	levelOrderDump(root4)
	fmt.Println(" -> ")
	levelOrderDump(result4)
}
