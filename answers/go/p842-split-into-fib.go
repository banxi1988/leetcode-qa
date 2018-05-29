package main

import (
	"fmt"
)

func isFibnacciArray([]int arr) bool{
	for i := 0; i < len(arr) - 2; i++{
		f1 := arr[i]
		f2 := arr[i+1]
		f3 := arr[i + 2]
		if f1 < 0 || f2 < 0 || f3 < 0{
			return false
		}

		if f1 + f2 != f3 {
			return false
		}
	}
	return true
}

func splitIntoFibonacci(S string) []int {
	bytes := []byte(S)
	nums := []int{}
	for f1Len := 1; f1Len < len(bytes) /3;f1Len ++{
		current := 0
		f2slice =
	}
}

func main() {
	fmt.Println("[123 456 579] -> ", splitIntoFibonacci("123456579"))
	fmt.Println("[1 1 2 3 5 8 13] -> ", splitIntoFibonacci("11235813"))
}
