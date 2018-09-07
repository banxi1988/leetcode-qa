package leetcode

import (
	"fmt"
)

func leafsOfTree(root *TreeNode) []int {
	leafs := []int{}
	if root == nil {
		return leafs
	}
	levelStacks := []*TreeNode{root}
	for len(levelStacks) > 0 {
		branch := levelStacks[0]
		levelStacks = levelStacks[1:]
		left := branch.Left
		right := branch.Right
		if left != nil {
			levelStacks = append(levelStacks, left)
		}
		if right != nil {
			levelStacks = append(levelStacks, right)
		}
		if left == nil && right == nil {
			leafs = append(leafs, branch.Val)
		}
	}
	return leafs
}

func collectLeafs(root *TreeNode, leafs *[]int) {
	if root == nil {
		return
	}
	if root.Left == nil && root.Right == nil {
		*leafs = append(*leafs, root.Val)
		return
	}
	if root.Left != nil {
		collectLeafs(root.Left, leafs)
	}
	if root.Right != nil {
		collectLeafs(root.Right, leafs)
	}
}

func deepEqual(arr1, arr2 []int) bool {
	arrLen := len(arr1)
	if arrLen != len(arr2) {
		return false
	}
	for i, num := range arr1 {
		if num == arr2[i] {
			continue
		} else {
			return false
		}
	}
	return true
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leafs1 := []int{}
	leafs2 := []int{}
	collectLeafs(root1, &leafs1)
	collectLeafs(root2, &leafs2)
	fmt.Println("leafs1:", leafs1)
	fmt.Println("leafs2:", leafs2)
	return deepEqual(leafs1, leafs2)
}
