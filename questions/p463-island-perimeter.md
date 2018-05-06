You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:


### 解题说明

遍历每一个格子，判断每一个格子增加的周长。

```go
calcCellPerimeter := func(row, col int) int {
		sides := 0
		// top
		if row == 0 || grid[row-1][col] == 0 {
			sides++
		}
		// right
		if col == (cols-1) || grid[row][col+1] == 0 {
			sides++
		}
		// bottom
		if row == (rows-1) || grid[row+1][col] == 0 {
			sides++
		}
		// left
		if col == 0 || grid[row][col-1] == 0 {
			sides++
		}
		return sides
	}
```