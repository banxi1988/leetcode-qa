package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leftUnivaluePath(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftLen := 0
	rootVal := root.Val
	left := root.Left
	for left != nil {
		if left.Val == rootVal {
			leftLen++
			if left.Left != nil {
				left = left.Left
			} else {
				break
			}
		} else {
			break
		}
	}
	leftLen += rightUnivaluePath(left)
	return leftLen
}

func rightUnivaluePath(root *TreeNode) int {
	if root == nil {
		return 0
	}
	rootVal := root.Val
	rightLen := 0
	right := root.Right
	for right != nil {
		if right.Val == rootVal {
			rightLen++
			if right.Right != nil {
				right = right.Right
			} else {
				break
			}
		} else {
			break
		}
	}
	rightLen += leftUnivaluePath(right)
	return rightLen
}

func univaluePath(root *TreeNode) int {
	leftLen := leftUnivaluePath(root)
	rightLen := rightUnivaluePath(root)
	return leftLen + rightLen
}

func longestUnivaluePathV1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	maxLen := 0
	branches := []*TreeNode{root}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		branchLen := univaluePath(branch)
		if branchLen > maxLen {
			maxLen = branchLen
		}
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
	}
	return maxLen
}
// https://blog.csdn.net/qq_36734094/article/details/78507945
func countPath(root *TreeNode, root2 *TreeNode, maxLen *int) int {
	if root == nil {
		return 0
	}
	leftLen := countPath(root.Left, root, maxLen)
	rightLen := countPath(root.Right, root, maxLen)
	if root.Left != nil && root.Left.Val == root.Val {
		leftLen += 1
	} else {
		leftLen = 0
	}

	if root.Right != nil && root.Right.Val == root.Val {
		rightLen += 1
	} else {
		rightLen = 0
	}

	if (leftLen + rightLen) > *maxLen {
		*maxLen = (leftLen + rightLen)
	}

	if leftLen > rightLen {
		return leftLen
	}
	return rightLen
}

func longestUnivaluePath(root *TreeNode) int {
	if root == nil {
		return 0
	}
	maxLen := 0
	countPath(root, root, &maxLen)
	return maxLen
}

func main() {
	root := &TreeNode{Val: 5}
	root.Left = &TreeNode{Val: 4}
	root.Right = &TreeNode{Val: 5}
	root.Left.Left = &TreeNode{Val: 1}
	root.Left.Right = &TreeNode{Val: 1}
	root.Right.Right = &TreeNode{Val: 5}
	fmt.Println("2 -> ", longestUnivaluePath(root))

	root1 := &TreeNode{Val: 5}
	root1.Left = &TreeNode{Val: 4}
	root1.Right = &TreeNode{Val: 5}
	root1.Left.Left = &TreeNode{Val: 1}
	root1.Left.Right = &TreeNode{Val: 1}
	root1.Right.Left = &TreeNode{Val: 5}
	fmt.Println("2 -> ", longestUnivaluePath(root1))

	root2 := &TreeNode{Val: 1}
	root2.Left = &TreeNode{Val: 4}
	root2.Right = &TreeNode{Val: 5}
	root2.Left.Left = &TreeNode{Val: 4}
	root2.Left.Right = &TreeNode{Val: 4}
	root2.Right.Right = &TreeNode{Val: 5}
	fmt.Println("2 -> ", longestUnivaluePath(root2))

	root3 := &TreeNode{Val: 5}
	fmt.Println("0 -> ", longestUnivaluePath(root3))

	root4 := &TreeNode{Val: 1}
	root4.Left = &TreeNode{Val: 4}
	root4.Right = &TreeNode{Val: 5}
	root4.Left.Left = &TreeNode{Val: 4}
	root4.Left.Right = &TreeNode{Val: 4}
	root4.Left.Left.Left = &TreeNode{Val: 4}
	fmt.Println("3 -> ", longestUnivaluePath(root4))

	root5 := &TreeNode{Val: 5}
	root5.Left = &TreeNode{Val: 5}
	root5.Right = &TreeNode{Val: 4}
	root5.Left.Left = &TreeNode{Val: 5}
	root5.Left.Right = &TreeNode{Val: 5}
	root5.Left.Left.Left = &TreeNode{Val: 5}
	fmt.Println("3 -> ", longestUnivaluePath(root5))

	// input1 := `1,5,8,9,7,7,8,1,4,8,1,9,0,8,7,1,7,4,2,9,8,2,4,null,null,9,null,null,null,6,0,9,4,1,0,1,8,9,0,1,8,9,1,0,9,6,2,5,null,2,3,0,2,4,8,8,8,5,0,0,9,4,9,1,null,0,7,2,2,3,null,6,1,0,8,9,9,9,4,8,4,3,4,4,0,null,null,8,3,8,null,null,0,null,0,4,9,1,2,null,4,4,0,4,3,5,5,7,4,1,6,null,1,0,null,null,null,2,8,7,7,null,null,0,2,5,5,9,3,3,null,7,6,6,7,9,8,1,7,7,7,2,6,null,7,null,4,6,4,6,null,null,9,1,null,null,null,5,5,5,4,2,2,8,5,1,1,3,1,3,7,null,2,null,9,1,4,4,7,7,null,1,5,6,2,7,3,null,9,1,null,2,4,4,8,null,null,7,null,6,null,7,4,3,5,8,4,8,5,null,null,8,null,null,null,4,4,null,null,null,null,8,3,5,5,null,null,null,1,2,0,null,null,9,3,null,8,3,7,1,8,9,0,1,8,2,null,4,null,null,8,null,null,null,null,2,null,4,8,5,5,3,1,null,null,6,null,1,null,null,6,null,null,null,null,7,3,null,null,null,8,6,4,null,6,9,0,7,8,null,null,0,6,7,null,null,0,0,7,2,3,2,null,0,2,3,null,0,1,7,9,0,7,null,null,null,null,5,8,2,6,3,2,0,4,null,null,0,9,1,1,1,null,1,3,null,7,9,1,3,3,8,null,null,null,null,6,null,null,null,null,9,8,1,3,8,3,0,6,null,null,8,5,6,5,2,1,null,5,null,7,0,0,null,9,3,9,null,3,0,0,9,1,7,0,2,null,6,8,5,null,null,null,null,null,7,null,2,5,null,null,9,null,null,null,null,null,null,null,null,null,null,null,4,1,null,3,6,6,2,5,5,9,null,null,7,8,null,null,2,7,3,7,2,5,null,1,3,4,null,null,8,3,6,9,null,1,null,null,null,null,9,7,5,2,null,5,null,6,4,5,null,1,2,0,6,null,1,6,null,null,5,null,7,8,4,7,8,6,4,null,5,6,7,9,1,0,4,null,null,null,6,4,8,4,5,null,0,4,4,0,1,7,1,null,1,null,3,6,null,null,null,null,8,null,5,0,7,5,null,null,5,8,null,null,3,null,null,8,null,2,4,null,null,null,null,null,null,null,9,null,9,null,9,null,null,null,null,7,1,null,null,2,null,null,5,5,5,5,6,4,null,null,1,6,4,0,null,0,6,3,0,null,5,5,null,null,null,null,2,null,3,6,null,3,0,5,0,1,0,3,4,9,9,2,7,3,8,6,9,null,5,8,null,null,null,null,9,8,0,7,null,null,8,8,6,6,0,2,7,4,2,3,8,6,4,null,8,null,null,null,2,0,null,1,3,5,4,2,2,5,8,8,null,3,0,null,1,6,0,null,null,9,null,2,null,6,8,2,null,null,5,null,null,null,9,6,6,4,2,0,null,null,1,null,0,null,null,null,6,6,null,null,null,4,7,9,null,0,1,null,null,9,null,null,null,4,null,8,null,null,null,null,null,null,4,null,6,null,3,null,null,5,1,2,5,null,0,7,8,null,7,null,null,4,null,4,4,null,2,null,6,null,null,null,7,null,null,null,null,6,4,null,6,null,6,9,null,null,null,9,6,null,9,null,3,null,2,null,7,7,null,null,0,null,6,3,null,null,null,null,null,null,1,null,null,null,6,9,7,null,7,null,9,3,3,null,null,null,null,4,null,null,3,null,null,null,3,9,null,0,3,1,9,6,7,9,4,8,null,null,6,null,1,3,7,null,null,null,3,null,2,null,8,1,1,null,null,6,null,7,3,5,null,6,3,4,null,null,5,7,1,null,null,6,4,6,null,null,null,null,5,7,0,7,0,null,5,8,5,5,4,5,null,null,null,null,null,null,1,7,null,null,7,null,9,9,6,4,null,null,3,2,1,null,0,null,0,6,null,null,null,1,5,null,null,null,8,null,null,null,null,3,4,8,null,null,9,6,4,null,null,null,null,8,9,null,1,null,null,null,7,null,null,null,null,null,9,null,null,null,4,1,6,7,0,null,null,null,7,null,null,8,null,null,null,null,null,null,null,4,null,9,null,null,null,null,3,0,6,null,5,null,9,9,null,null,4,3,4,null,null,null,null,8,null,5,null,null,null,null,5,2,null,null,null,null,null,null,null,2,null,null,2,1,8,5,null,0,null,0,3,2,4,5,null,null,null,null,null,7,null,null,0,null,0,null,null,null,0,3,9,null,null,null,null,5,null,null,0,5,0,0,null,9,null,null,null,null,null,null,null,null,8,null,9,3,5,9,0,5,9,null,null,9,4,null,0,2,0,null,null,7,null,7,null,5,7,8,7,null,null,null,3,0,3,null,null,null,null,null,4,5,null,null,2,3,null,2,null,null,7,null,null,9,null,null,9,7,1,null,null,1,6,1,8,null,null,5,null,null,3,7,9,6,null,null,null,null,1,null,null,null,3,7,3,2,3,3,null,1,null,null,null,1,null,null,4,3,4,8,7,null,0,3,0,null,1,1,null,null,null,null,null,5,null,6,0,null,3,1,null,6,null,null,4,0,1,null,6,1,null,null,9,6,4,9,0,8,9,3,3,6,null,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,5,8,3,5,4,null,6,null,0,null,null,6,null,4,3,null,null,null,null,null,null,null,null,null,null,null,null,null,null,7,3,null,null,1,null,2,4,null,null,null,6,null,null,null,6,null,5,null,null,null,null,1,null,null,3,null,1,null,7,1,null,null,7,1,3,4,8,null,null,null,null,null,4,null,null,4,null,null,null,7,null,6,null,null,1,null,null,null,7,3,3,null,null,null,null,3,0,null,null,4,null,null,null,null,null,null,null,null,null,null,8,null,null,9,null,null,6,6,5,2,null,8,3,8,null,null,null,null,6,7,0,null,null,null,null,1,1,5,null,0,5,null,5,null,null,null,1,2,null,2,9,1,null,2,4,1,null,null,null,1,8,4,4,5,2,null,null,6,4,7,5,2,9,null,4,null,null,null,null,null,3,null,null,5,9,null,null,null,null,9,null,9,null,null,null,2,null,1,9,null,null,null,null,null,1,9,3,null,null,1,9,null,5,2,1,0,null,null,1,9,8,4,7,null,null,5,7,null,null,null,null,1,2,8,null,6,0,null,null,null,null,0,null,null,null,6,null,2,3,0,9,null,null,1,4,6,null,8,null,null,5,null,3,0,null,6,null,null,null,null,null,2,null,null,null,null,null,null,2,5,8,6,9,null,null,null,8,null,null,9,6,null,null,null,null,3,null,null,null,null,9,null,null,2,null,null,null,null,null,null,8,8,null,null,null,null,null,9,null,6,null,2,5,null,null,1,2,null,4,null,null,4,null,null,3,5,null,3,3,null,null,1,null,null,null,null,4,null,2,3,null,4,5,3,null,7,null,null,null,7,6,null,null,1,3,null,4,9,8,null,null,0,null,3,4,null,8,null,1,null,null,2,2,null,null,4,null,null,null,3,null,null,2,null,null,null,4,null,5,null,null,null,null,2,null,5,null,null,null,null,null,null,2,7,5,null,6,null,null,null,null,2,null,0,null,3,null,1,null,9,4,null,3,null,null,null,null,null,null,null,5,5,7,null,null,1,null,4,6,null,null,null,2,null,5,9,0,6,2,null,null,null,null,null,null,null,null,null,null,null,null,5,null,7,null,2,9,null,null,1,null,null,null,1,6,null,6,null,null,0,8,null,4,null,null,null,null,4,null,null,0,null,6,0,null,null,null,4,null,null,null,null,null,0,null,null,null,null,null,null,null,null,null,null,null,null,0,5,4,2,6,4,5,3,4,null,null,5,null,null,null,null,4,null,null,3,6,2,0,null,6,6,null,null,null,null,0,6,null,null,null,3,9,4,null,null,null,null,null,0,null,null,6,7,0,null,9,2,null,3,3,null,null,8,null,3,null,null,null,8,5,3,null,2,4,null,9,6,9,null,null,null,null,6,null,6,null,5,3,null,null,null,null,4,null,null,null,9,0,9,7,1,1,null,1,null,1,6,null,5,null,6,null,null,1,null,null,null,null,null,null,5,null,null,null,null,null,3,null,6,1,null,0,2,null,null,0,null,null,0,null,null,null,null,null,3,null,null,8,null,null,5,3,3,null,null,null,null,null,null,null,3,null,null,0,8,7,null,null,8,1,null,null,null,null,null,null,7,null,null,null,null,null,null,null,null,null,null,null,5,2,null,2,6,null,null,null,null,null,null,null,1,5,0,null,null,2,null,7,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,3,null,null,4,null,null,2,null,null,null,null,0,3,null,null,null,null,null,7,null,8,null,null,null,null,8,5,null,3,4,null,null,null,8,null,null,null,null,null,null,null,null,null,3,7,null,null,null,4,0,3,null,null,6,null,null,null,null,null,null,null,null,null,null,null,null,8,null,null,null,null,null,2,null,null,null,null,null,null,null,null,null,0,null,null,null,2,null,null,null,8,2,null,null,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,2,null,null,null,2,5,null,null,null,null,null,null,null,null,null,null,null,2,null,null,null,null,null,8,null,null,null,null,null,null,null,null,null,null,0,5`
	// expect 2
}
