Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


首先实现一个返回一维数组的层次遍历的算法：

```go
func levelOrderBottom(root *TreeNode) []int {
	values := []int{}
	if root == nil {
		return values
	}
	branches := []*TreeNode{root}
	for len(branches) > 0 {
		branch := branches[0]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
		branches = branches[1:]
		values = append(values, branch.Val)
	}

	return values
}
```

在要返回二维数据的问题上，一度陷入了困境。
通过引入一个 `nodeDepthMap` 来记录分支的深度，然后再使用数组，得到下面的结果。但是还是从上到下的。


```go
func levelOrderBottom(root *TreeNode) [][]int {
	arrarr := [][]int{}
	if root == nil {
		return arrarr
	}
	branches := []*TreeNode{root}
	nodeDepthMap := make(map[*TreeNode]int)
	nodeDepthMap[root] = 0

	for len(branches) > 0 {
		branch := branches[0]
		branchDepth := nodeDepthMap[branch]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
			nodeDepthMap[branch.Left] = branchDepth + 1
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
			nodeDepthMap[branch.Right] = branchDepth + 1
		}
		branches = branches[1:]
		if len(arrarr) > branchDepth {
			arrarr[branchDepth] = append(arrarr[branchDepth], branch.Val)
		} else {
			arrarr = append(arrarr, []int{branch.Val})
		}
	}

	return arrarr

}
```

暂时的一个解法办法就是，遍历之后 reverse 一下:

```go
	// reverse
	for i, j := 0, len(arrarr)-1; i < j; i, j = i+1, j-1 {
		tmp := arrarr[i]
		arrarr[i] = arrarr[j]
		arrarr[j] = tmp
	}

```