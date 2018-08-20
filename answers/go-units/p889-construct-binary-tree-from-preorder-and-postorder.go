package leetcode

func indexOfInts(a []int, x int) int {
	for i, num := range a {
		if num == x {
			return i
		}
	}
	return -1
}

func constructFromPrePost(pre []int, post []int) *TreeNode {
	valueLen := len(pre)
	if valueLen == 0 {
		return nil
	}
	rootVal := pre[0]
	root := &TreeNode{Val: rootVal}
	if valueLen > 1 {
		// 最后一个是 rootVal,那倒数第二个是右分支的值
		rightBranchValue := post[valueLen-2]
		// 那此时以 rightBranchValue 为分割点，左边是左子树的值，右边是右子树的值
		preIndex := indexOfInts(pre, rightBranchValue)
		preLeft := pre[1:preIndex]
		preRight := pre[preIndex:]
		leftBranchValue := pre[1]
		postRight := []int{}
		postLeft := []int{}
		postIndex := indexOfInts(post, leftBranchValue)
		if leftBranchValue == rightBranchValue {
			postRight = post[0 : postIndex+1]
		} else {
			postLeft = post[0 : postIndex+1]
			postRight = post[postIndex+1 : valueLen-1]
		}

		root.Left = constructFromPrePost(preLeft, postLeft)
		root.Right = constructFromPrePost(preRight, postRight)
	}
	return root
}
