Given an m \* n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input:
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation:
Initially, M =
[[0, 0, 0],
[0, 0, 0],
[0, 0, 0]]

After performing [2,2], M =
[[1, 1, 0],
[1, 1, 0],
[0, 0, 0]]

After performing [3,3], M =
[[2, 2, 1],
[2, 2, 1],
[1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.

开始采用的是暴力的方式：

```go
unc maxCount(m int, n int, ops [][]int) int {
	opsCount := len(ops)
	if opsCount < 1 {
		return m * n
	}
	if opsCount == 1 {
		op := ops[0]
		return op[0] * op[1]
	}
	// 暴力
	grid := make([][]int, m)
	for i := 0; i < m; i++ {
		grid[i] = make([]int, n)
	}
	maxNum := 0
	for _, op := range ops {
		rows := op[0]
		cols := op[1]
		for i := 0; i < rows; i++ {
			for j := 0; j < cols; j++ {
				num := grid[i][j]
				num++
				grid[i][j] = num
				if num > maxNum {
					maxNum = num
				}
			}
		}
	}

	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == maxNum {
				count++
			}
		}
	}
	return count

}
```

但是这样会超时。

考虑到他们都是从左上角为起点的，只要取所以的操作数的交集就可以了。即最短宽和高。于是得到如下解法：

```go
func maxCount(m int, n int, ops [][]int) int {
	minCols := n
	minRows := m
	for _, op := range ops {
		row := op[0]
		col := op[1]
		if row < minRows {
			minRows = row
		}
		if col < minCols {
			minCols = col
		}
	}
	return minRows * minCols
}
```
