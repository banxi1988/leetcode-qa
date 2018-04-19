package main

import "fmt"
import "strings"
import "strconv"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePathsInt(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}
	if root.Left == nil && root.Right == nil {
		return [][]int{{root.Val}}
	}
	leftPaths := binaryTreePathsInt(root.Left)
	rightPaths := binaryTreePathsInt(root.Right)
	paths := [][]int{}
	for i := 0; i < len(leftPaths); i++ {
		path := leftPaths[i]
		if len(path) > 0 {
			path = append([]int{root.Val}, path...)
			paths = append(paths, path)
		}
	}
	for i := 0; i < len(rightPaths); i++ {
		path := rightPaths[i]
		if len(path) > 0 {
			path = append([]int{root.Val}, path...)
			paths = append(paths, path)
		}
	}
	return paths
}

func join(arr []int, sep string) string {
	numCount := len(arr)
	if numCount == 0 {
		return ""
	}
	strs := make([]string, numCount)
	for i := 0; i < numCount; i++ {
		strs[i] = strconv.Itoa(arr[i])
	}
	return strings.Join(strs, sep)
}

func binaryTreePaths(root *TreeNode) []string {
	paths := binaryTreePathsInt(root)
	strPaths := make([]string, len(paths))
	for i := 0; i < len(paths); i++ {
		path := paths[i]
		strPaths[i] = join(path, "->")
	}
	return strPaths
}

func main() {
	root1 := &TreeNode{Val: 1}
	root1.Left = &TreeNode{Val: 2}
	root1.Left.Right = &TreeNode{Val: 5}
	root1.Right = &TreeNode{Val: 3}

	path1 := binaryTreePaths(root1)
	fmt.Println("expect [1->2->5, 1->3] actual", path1)
}
