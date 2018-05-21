package main

import (
	"fmt"
)

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}

const (
	MaxSum = int(1e7*2 + 1)
)

func hash(a, b int) int {
	// remove negative number
	a += 1e7
	b += 1e7
	if a > b {
		return MaxSum*a + b
	} else {
		return MaxSum*b + a
	}
}

func findPairs(nums []int, k int) int {
	pairsMap := make(map[int]bool)
	for i := 0; i < len(nums)-1; i++ {
		numi := nums[i]
		for j := i + 1; j < len(nums); j++ {
			numj := nums[j]
			diff := abs(numj - numi)
			if diff == k {
				key := hash(numi, numj)
				// _, ok := pairsMap[key]
				// if !ok {
				// 	fmt.Print("(", numi, ",", numj, ")")
				// }
				pairsMap[key] = true

			}
		}
	}
	return len(pairsMap)
}
func main() {
	fmt.Println("2 -> ", findPairs([]int{3, 1, 4, 1, 5}, 2))
	fmt.Println("4 -> ", findPairs([]int{1, 2, 3, 4, 5}, 1))
	fmt.Println("1 -> ", findPairs([]int{1, 3, 1, 5, 4}, 0))
}
