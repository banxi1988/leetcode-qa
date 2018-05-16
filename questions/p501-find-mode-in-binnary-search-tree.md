Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


## 解答分析

### 首先是一个使用了 map 保存数据的解法：

1) 遍历 Tree 得到 num->count 的map。 并记录最大的 count 即 maxCount
2) 筛选出 count == maxCount 的节点值。

```go
func findMode(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	maxCount := 0
	nodeCountMap := make(map[int]int)
	branches := []*TreeNode{root}
	for len(branches) > 0 {
		branch := branches[0]
		branches = branches[1:]
		if branch.Left != nil {
			branches = append(branches, branch.Left)
		}
		if branch.Right != nil {
			branches = append(branches, branch.Right)
		}
		count, _ := nodeCountMap[branch.Val]
		count++
		nodeCountMap[branch.Val] = count
		if count > maxCount {
			maxCount = count
		}
	}

	result := []int{}
	for num,count := range nodeCountMap {
		if count == maxCount {
			result = append(result, num)
		}
	}
	return result
}
```

### 其他解法

在上面提解法中，有一个特点没有利用上，就是此树是一棵二叉搜索树。

考虑递归

1） 终止条件。`Left` 和 `Right` 为 `nil`

