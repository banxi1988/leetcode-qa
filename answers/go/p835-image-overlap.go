package main

import "fmt"

// 有多大的可重叠区域，任意移到两个图片。
// 如果可能不移到是有最大重叠区域的。

func overlapCount(img1, img2 [][]int) int {
	count := 0
	for i := 0; i < len(img1); i++ {
		for j := 0; j < len(img1[0]); j++ {
			if img1[i][j] == 1 && img2[i][j] == 1 {
				count++
			}
		}
	}
	return count
}

const (
	Down  = 0
	Up    = 1
	Right = 2
	Left  = 3
)

func clipRect(arr [][]int, rows, cols, rowDirection int, colDirection int) [][]int {
	rowCount := len(arr)
	colCount := len(arr[0])
	remainRows := rowCount - rows
	remainCols := colCount - cols

	rect := [][]int{}
	for i := 0; i < remainRows; i++ {
		rowIndex := i
		if rowDirection == Up {
			rowIndex = rows + i
		}
		row := arr[rowIndex]
		if colDirection == Right {
			rowSlice := row[0:remainCols]
			rect = append(rect, rowSlice)
		} else {
			rowSlice := row[cols:colCount]
			rect = append(rect, rowSlice)
		}
	}
	return rect
}

func largestOverlap(A [][]int, B [][]int) int {
	size := len(A)
	rowCount := size
	colCount := size
	maxOverlap := 0
	// i,j row and col slide count
	var sliceA [][]int
	var sliceB [][]int
	overlap := 0
	for i := 0; i < rowCount; i++ {
		for j := 0; j < colCount; j++ {
			////// move down
			// move Right
			sliceA = clipRect(A, i, j, Down, Right)
			sliceB = clipRect(B, i, j, Up, Left)
			overlap = overlapCount(sliceA, sliceB)
			// if i == 1 && j == 1 {
			// 	fmt.Println("slice A:", sliceA)
			// 	fmt.Println("slice B:", sliceB)
			// 	fmt.Println("expected overlap 3: ", overlap)
			// }
			if overlap > maxOverlap {
				maxOverlap = overlap
			}
			// move Left
			sliceA = clipRect(A, i, j, Down, Left)
			sliceB = clipRect(B, i, j, Up, Right)
			overlap = overlapCount(sliceA, sliceB)
			if overlap > maxOverlap {
				maxOverlap = overlap
			}
			////// move up
			sliceA = clipRect(A, i, j, Up, Right)
			sliceB = clipRect(B, i, j, Down, Left)
			overlap = overlapCount(sliceA, sliceB)
			if overlap > maxOverlap {
				maxOverlap = overlap
			}
			sliceA = clipRect(A, i, j, Up, Left)
			sliceB = clipRect(B, i, j, Down, Right)
			overlap = overlapCount(sliceA, sliceB)
			if overlap > maxOverlap {
				maxOverlap = overlap
			}
		}
	}
	return maxOverlap
}
func main() {
	arrA := [][]int{
		{1, 1, 0},
		{0, 1, 0},
		{0, 1, 0},
	}
	arrB := [][]int{
		{0, 0, 0},
		{0, 1, 1},
		{0, 0, 1},
	}
	fmt.Println("3 -> ", largestOverlap(arrA, arrB))

	arrA2 := [][]int{
		{0, 1},
		{1, 1},
	}
	arrB2 := [][]int{
		{1, 1},
		{1, 0},
	}
	fmt.Println("2 -> ", largestOverlap(arrA2, arrB2))
}
