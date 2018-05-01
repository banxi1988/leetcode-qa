package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSumWithStartNode(start *TreeNode, sum int) int {
	if start == nil {
		return 0
	}
	count := 0
	if start.Val == sum {
		count++
	}
	count += pathSumWithStartNode(start.Left, sum-start.Val)
	count += pathSumWithStartNode(start.Right, sum-start.Val)

	return count
}

// The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}
	startNodes := []*TreeNode{root}
	count := 0
	for len(startNodes) > 0 {
		startNode := startNodes[0]
		startNodes = startNodes[1:]
		count += pathSumWithStartNode(startNode, sum)

		if startNode.Left != nil {
			startNodes = append(startNodes, startNode.Left)
		}
		if startNode.Right != nil {
			startNodes = append(startNodes, startNode.Right)
		}
	}
	return count
}

func main() {
	root1 := &TreeNode{Val: 10}

	root1.Left = &TreeNode{Val: 5}
	root1.Right = &TreeNode{Val: -3}

	root1.Left.Left = &TreeNode{Val: 3}
	root1.Left.Right = &TreeNode{Val: 2}
	root1.Right.Right = &TreeNode{Val: 11}

	root1.Left.Left.Left = &TreeNode{Val: 3}
	root1.Left.Left.Right = &TreeNode{Val: -2}
	root1.Left.Right.Right = &TreeNode{Val: 1}

	fmt.Println(" 3 -> ", pathSum(root1, 8))

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 2}

	fmt.Println("1 ->", pathSum(root2, 2))

	root3 := &TreeNode{Val: 5}
	root3.Left = &TreeNode{Val: 4}
	root3.Right = &TreeNode{Val: 8}

	root3.Left.Left = &TreeNode{Val: 11}
	root3.Left.Right = nil

	root3.Right.Left = &TreeNode{Val: 13}
	root3.Right.Right = &TreeNode{Val: 4}

	root3.Left.Left.Left = &TreeNode{Val: 7}
	root3.Left.Left.Right = &TreeNode{Val: 2}

	root3.Right.Right.Left = &TreeNode{Val: 5}
	root3.Right.Right.Right = &TreeNode{Val: 1}
	fmt.Println("3 ->", pathSum(root3, 22))

}
