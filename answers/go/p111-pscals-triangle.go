package main

import "fmt"

func generate(numRows int) [][]int {
	arrarr := [][]int{}
	if numRows < 1 {
		return arrarr
	}
	arrarr = append(arrarr, []int{1})
	if numRows == 1 {
		return arrarr
	}
	prevArr := []int{1, 1}
	arrarr = append(arrarr, prevArr)
	if numRows == 2 {
		return arrarr
	}
	for rowIndex := 2; rowIndex < numRows; rowIndex++ {
		curArr := []int{1}
		for colIndex := 0; colIndex < len(prevArr)-1; colIndex++ {
			num := prevArr[colIndex] + prevArr[colIndex+1]
			curArr = append(curArr, num)
		}
		curArr = append(curArr, 1)
		arrarr = append(arrarr, curArr)
		prevArr = curArr
	}
	return arrarr
}

func main() {
	fmt.Println(generate(1))

}
