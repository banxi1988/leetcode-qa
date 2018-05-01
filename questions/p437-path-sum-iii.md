You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


一开始最容易想到的是哪下的递归代码：

```go
func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}
	count := 0
    if root.Left == nil && root.Right == nil {
        return 1
    }
	parents := []*TreeNode{root}
	for len(parents) > 0 {
		parent := parents[0]
		parents = parents[1:]
		if parent.Left != nil {
			leftCount := pathSum(parent.Left, sum-parent.Val)
			count += leftCount
			parents = append(parents, parent.Left)
		}
		if parent.Right != nil {
			rightCount := pathSum(parent.Right, sum-parent.Val)
			count += rightCount
			parents = append(parents, parent.Right)
		}
	}
	return count
}
```

但是由于上面的返回条件是 `root.Left == nil && root.Right == nil` 所以它计算的是所有到啥叶子节点的路径。
像上面的 5-3 的组合就没有算在其中。

做了一点改进就是:

```go
	if root.Val == sum {
		if root.Left == nil && root.Right == nil {
			return 1
		}
		count++
	}
```

并且满足条件,但是不是叶子那么就 `count++`， 后面的操作继续 。

但是测试下来上面的代码还是有一个问题就是对于。
`(1->2), 2` 这种只有一个叶子分支的。 预期是要返回 1， 但是计算返回的是 0.

相当于是代码执行到了这里:

```go
			leftCount := pathSum(parent.Left, 2-1) // 此时 parent.Left.Val == 2
			count += leftCount
			parents = append(parents, parent.Left)
```

后面对于分支的判断就出错了。

所以把判断分成这样的逻辑。

1） 以一个点作为必须的起始点，判断以其作为起始点的路径总数。

计算方法如下：

```go
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
```

2) 遍历各点作为起始点的情况,然后累加：

```go
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
```