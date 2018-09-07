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

func distanceKByRoot(root *TreeNode, K int) []int {
	levelStacks := []*TreeNode{root}
	nodeLevelMap := make(map[*TreeNode]int)
	nodeLevelMap[root] = 0
	results := []int{}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		branchLevel, _ := nodeLevelMap[branch]
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if branchLevel == K {
			results = append(results, branch.Val)
		}
		curLevel := branchLevel + 1
		if curLevel <= K {
			if left != nil {
				levelStacks = append(levelStacks, left)
				nodeLevelMap[left] = curLevel
			}
			if right != nil {
				levelStacks = append(levelStacks, right)
				nodeLevelMap[right] = curLevel
			}
		}
	}
	return results
}

func distanceRooToTarget(root *TreeNode, target int) int {
	levelStacks := []*TreeNode{root}
	nodeLevelMap := make(map[*TreeNode]int)
	nodeLevelMap[root] = 0
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		branchLevel, _ := nodeLevelMap[branch]
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if branch.Val == target {
			return branchLevel
		}
		curLevel := branchLevel + 1
		if left != nil {
			levelStacks = append(levelStacks, left)
			nodeLevelMap[left] = curLevel
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
			nodeLevelMap[right] = curLevel
		}
	}
	return -1
}

func distanceK(root *TreeNode, target *TreeNode, K int) []int {
	// nodes := []*TreeNode{root}
	// results := []int{}
	// targetDistance := distanceRooToTarget(root, target.Val)
	levelStacks := []*TreeNode{root}
	nodeLevelMap := make(map[*TreeNode]int)
	nodeLevelMap[root] = 0
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		branchLevel, _ := nodeLevelMap[branch]
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if branch.Val == target.Val {
		}
		curLevel := branchLevel + 1
		if left != nil {
			levelStacks = append(levelStacks, left)
			nodeLevelMap[left] = curLevel
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
			nodeLevelMap[right] = curLevel
		}
	}
	results1 := distanceKByRoot(target, K)
	return results1
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

	fmt.Println("[6,2,0,8] -> ", distanceKByRoot(root, 2))
	fmt.Println("[7,4] -> ", distanceKByRoot(root, 3))
	fmt.Println("[5,1] -> ", distanceKByRoot(root, 1))
	fmt.Println("[3] -> ", distanceKByRoot(root, 0))
	fmt.Println("1 -> ", distanceRooToTarget(root, 5))
	fmt.Println("1 -> ", distanceRooToTarget(root, 1))
	fmt.Println("2 -> ", distanceRooToTarget(root, 6))
	fmt.Println("2 -> ", distanceRooToTarget(root, 8))
	fmt.Println("3 -> ", distanceRooToTarget(root, 7))
	target := root.Left
	fmt.Println("[7,4,1] -> ", distanceK(root, target, 2))
}
