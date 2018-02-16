package main 
import "fmt"

type TreeNode struct{
	Val int
	Left *TreeNode
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

 func findValue(root *TreeNode, value int) bool{
	if root == nil{
		return false 
	}
	if root.Val == value{
		return true
	}else if root.Val > value{
		return findValue(root.Left, value)
	}else{
		return findValue(root.Right, value)
	}
 }

 func findTarget(root *TreeNode, k int) bool {
	 if root == nil {
		 return false
	 }

	 remain := k - root.Val
	 found := false
	 if remain < root.Val{
		found = findValue(root.Left, remain)
	 }else{
		found = findValue(root.Right, remain)
	 }
	 if found{
		 return true
	 }
	 found = findTarget(root.Left, k)
	 if found{
		 return true
	 }
	 return findTarget(root.Right, k)
}



func main(){
	root := TreeNode{Val:5}
	rootLeft := TreeNode{Val:3}
	rootRight := TreeNode{Val:6}
	rootLeft.Left = &TreeNode{Val:2}
	rootLeft.Right = &TreeNode{Val:4}

	rootRight.Right = &TreeNode{Val:7}

	root.Left = &rootLeft
	root.Right = &rootRight
	fmt.Println(root)
	fmt.Println(findTarget(&root, 9))

	root2 := TreeNode{Val:2}
	root2.Left = &TreeNode{Val:1}
	root2.Right = &TreeNode{Val:3}
	fmt.Println(findTarget(&root2, 4))

}