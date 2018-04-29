package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	sum := 0
	branches := []*TreeNode{root}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		left := branch.Left
		right := branch.Right
		if right != nil {
			branches = append(branches, right)
		}

		if left != nil {
			if left.Left == nil && left.Right == nil {
				sum += left.Val
			} else {
				branches = append(branches, left)
			}
		}

	}

	return sum
}

func main() {
	fmt.Println("0 -> ", sumOfLeftLeaves(nil))
	fmt.Println("0 -> ", sumOfLeftLeaves(&TreeNode{Val: 1}))

	root1 := &TreeNode{Val: 3}
	root1.Left = &TreeNode{Val: 9}
	root1.Right = &TreeNode{Val: 20}
	root1.Right.Left = &TreeNode{Val: 15}
	root1.Right.Right = &TreeNode{Val: 7}
	fmt.Println("24 -> ", sumOfLeftLeaves(root1))

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 2}
	root2.Right = &TreeNode{Val: 3}
	root2.Left.Left = &TreeNode{Val: 4}
	root2.Left.Right = &TreeNode{Val: 5}
	fmt.Println("4 -> ", sumOfLeftLeaves(root2))

}
