package main

import "fmt"

func product(arr1, arr2 []int) [][]int {
	// product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
	result := [][]int{}
	for i := 0; i < len(arr1); i++ {
		for j := 0; j < len(arr2); j++ {
			comb := []int{arr1[i], arr2[j]}
			result = append(result, comb)
		}
	}
	return result
}

func permutations(nums []int, r int) [][]int{
	n := len(nums)
	if r > n:
		return [][]int{}
	
}

func readBinaryWatchHour(num int) []int {
	if num < 1 {
		return []int{}
	}
	if num > 4 {
		return []int{}
	}
	return []int{}
}

// func readBinaryWatch(num int) []string {

// }

func main() {
	fmt.Println(product([]int{1, 2, 3, 4}, []int{5, 6}))
	fmt.Println("[1,2,4,8] ->", readBinaryWatchHour(1))
	// fmt.Println(readBinaryWatch(1))
}
