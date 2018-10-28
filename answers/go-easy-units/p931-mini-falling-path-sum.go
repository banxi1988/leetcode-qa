package geasy

import "math"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type findSumFuncType = func(row, prevCol, pathSum int)

/// [1,2,3]
/// [4,5,6]
/// [7,8,9]
func minFallingPathSum(A [][]int) int {
	rows := len(A)
	cols := rows
	if rows == 1 {
		return A[0][0]
	}
	minSum := math.MaxInt64
	var findSum findSumFuncType
	findSum = func(row, prevCol, pathSum int) {
		// last row
		minCol := max(0, prevCol-1)
		maxCol := min(cols-1, prevCol+1)
		if row == (rows - 1) {
			for col := minCol; col <= maxCol; col++ {
				finalSum := pathSum + A[row][col]
				if finalSum < minSum {
					minSum = finalSum
				}
			}
		} else {
			for col := minCol; col <= maxCol; col++ {
				newSum := pathSum + A[row][col]
				findSum(row+1, col, newSum)
			}
		}

	}

	for startCol := 0; startCol < cols; startCol++ {
		findSum(0, startCol, 0)
	}

	return minSum
}
