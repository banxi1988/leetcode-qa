package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func findValue(root *TreeNode, value int) bool {
	if root == nil {
		return false
	}
	if root.Val == value {
		return true
	} else if root.Val > value {
		return findValue(root.Left, value)
	} else {
		return findValue(root.Right, value)
	}
}

func findTarget(root *TreeNode, k int) bool {
	if root == nil {
		return false
	}
	// 1 ) 先判断根节点 参与的情况
	remind := k - root.Val
	found := false
	if remind < root.Val {
		found = findValue(root.Left, remind)
	} else {
		found = findValue(root.Right, remind)
	}
	if found {
		return true
	}
	// 2) 解全在左子树
	found = findTarget(root.Left, k)
	if found {
		return true
	}
	// 3) 解全在右子树
	found = findTarget(root.Right, k)
	if found {
		return true
	}
	// 4) 解一个在左子树，一个在右子树
	if root.Left == nil {
		return false
	}

	branches := []*TreeNode{root.Left}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		remind := k - branch.Val
		found = findValue(root.Right, remind)
		if found {
			return true
		}
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
	}
	return false
}

func main() {
	root := TreeNode{Val: 5}
	rootLeft := TreeNode{Val: 3}
	rootRight := TreeNode{Val: 6}
	rootLeft.Left = &TreeNode{Val: 2}
	rootLeft.Right = &TreeNode{Val: 4}

	rootRight.Right = &TreeNode{Val: 7}

	root.Left = &rootLeft
	root.Right = &rootRight
	fmt.Println("True -> ", findTarget(&root, 9))
	fmt.Println("False -> ", findTarget(&root, 28))

	root2 := TreeNode{Val: 2}
	root2.Left = &TreeNode{Val: 1}
	root2.Right = &TreeNode{Val: 3}
	// 这个 testCase 说明存在 可以不包含分支节点的解法的存在。
	// 如果将此二叉树转成数组再暴力求解，那 BST 的特点就没有用到了。
	// 另外二叉树本身的特点也没有用到。
	// 一般的递归方法在这种 testCase 不好处理。
	// 一开始的思路是选定一个数字之后再去找另外一个数字。
	// 现在对于这种 testCase 改一下思考。
	// 对于某一个分支开始判断。
	//  1. 如果  target < root.Val 那解肯定是在 root.Lef
	//  2. 如果 target > root.Val,这就复杂一点。
	//    1). 如果 target > root.Val * 2  说明 解肯定在右子树。
	//    2) 如果 target < root.Val * 2, 说明有一个数在 root.Left，一个数在 root.Right.
	//        这里由于不知道左边的数的值的大小，但是可以遍历左子数树的所有数。对于遍历的每一个数，
	//        判断是否在右子树存在对应的余值。

	fmt.Println("true ->", findTarget(&root2, 4))
	fmt.Println("true ->", findTarget(&root2, 3))

	root3 := &TreeNode{Val: 2}
	root3.Left = &TreeNode{Val: 0}
	root3.Right = &TreeNode{Val: 3}
	root3.Left.Left = &TreeNode{Val: -4}
	root3.Left.Right = &TreeNode{Val: 1}
	// 这个 testCase 说明上面的考虑还忽略了一点，就是其中值是负数的情况。 这样是无法判断解答是在左子树还是一定在右子树。
	// 所以还需要继续修改，
	//  1) 解在左子树。
	//  2) 解在右子树.
	//  3) 解的一个值在 root.Value ，其他的值在左子树或右子树
	//  4) 解的一个值在右子树，一个在右了树
	fmt.Println("true -> ", findTarget(root3, -1))
}
