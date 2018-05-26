package main

import "fmt"

func flipAndInvertImage(A [][]int) [][]int {
	rows := len(A)
	cols := len(A[0])
	for row := 0; row < rows; row++ {
		imgRow := A[row]
		for i, j := 0, (cols - 1); i < j; i, j = i+1, j-1 {
			tmp := imgRow[i]
			imgRow[i] = imgRow[j]
			imgRow[j] = tmp
		}
	}
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			pix := A[i][j]
			if pix == 0 {
				A[i][j] = 1
			} else {
				A[i][j] = 0
			}
		}
	}
	return A
}

func main() {
	arr1 := [][]int{
		{1, 1, 0},
		{1, 0, 1},
		{0, 0, 0},
	}
	fmt.Println("[[1,0,0],[0,1,0],[1,1,1]]  ->", flipAndInvertImage(arr1))
}
