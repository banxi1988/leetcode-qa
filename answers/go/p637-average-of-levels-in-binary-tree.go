package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sum(nums []int) int {
	s := 0
	for _, num := range nums {
		s += num
	}
	return s
}

func avg(nums []int) float64 {
	return float64(sum(nums)) / float64(len(nums))
}

func averageOfLevels(root *TreeNode) []float64 {
	levelStacks := []*TreeNode{root}
	levelMap := make(map[*TreeNode]int)
	levelMap[root] = 0
	levelNumsMap := make(map[int][]int)
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		level, _ := levelMap[branch]

		nums, _ := levelNumsMap[level]
		if nums == nil {
			nums = []int{}
		}
		nums = append(nums, branch.Val)
		levelNumsMap[level] = nums

		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
			levelMap[left] = level + 1
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
			levelMap[right] = level + 1
		}
	}

	result := make([]float64, len(levelNumsMap))
	for level, nums := range levelNumsMap {
		result[level] = avg(nums)
	}
	return result
}

func main() {
	root := &TreeNode{Val: 3}
	root.Left = &TreeNode{Val: 9}
	root.Right = &TreeNode{Val: 20}
	root.Right.Left = &TreeNode{Val: 15}
	root.Right.Right = &TreeNode{Val: 7}
	fmt.Println("[3, 14.5, 11] -> ", averageOfLevels(root))
}
