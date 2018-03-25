package main

import "fmt"

func getRow(rowIndex int) []int {
	row := rowIndex + 1
	if row < 1 {
		return []int{}
	}
	switch row {
	case 1:
		return []int{1}
	case 2:
		return []int{1, 1}
	case 3:
		return []int{1, 2, 1}
	case 4:
		return []int{1, 3, 3, 1}
	case 5:
		return []int{1, 4, 6, 4, 1}
	default:
		arr := []int{1, rowIndex}
		midIndex := row / 2
		cnk := rowIndex // C (maxN,1)
		for colIndex := 2; colIndex <= midIndex; colIndex++ {
			// C (N, K + 1) = C(N,K) * (n- k)/(k + 1)
			// C (maxN,2) = C (maxN, 1) * (maxN - 1) / ( 1 + 1)
			k := colIndex - 1
			cnk1 := cnk * (rowIndex - k) / (k + 1)
			arr = append(arr, cnk1)
			cnk = cnk1
		}
		// 对称
		midIndex = rowIndex / 2
		for colIndex := midIndex - 1; colIndex > 1; colIndex-- {
			arr = append(arr, arr[colIndex])
		}
		arr = append(arr, rowIndex)
		arr = append(arr, 1)
		return arr
	}

}

func main() {
	fmt.Println(getRow(8))

}
