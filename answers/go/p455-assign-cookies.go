package main

import "fmt"

import "sort"

func findContentChildren(greeds []int, sizes []int) int {
	sort.Ints(greeds)
	sort.Ints(sizes)
	minSizeIndex := 0
	contentCount := 0
	for i := 0; i < len(greeds); i++ {
		greed := greeds[i]
		for j := minSizeIndex; j < len(sizes); j++ {
			if sizes[j] >= greed {
				minSizeIndex = j + 1
				contentCount++
				break
			} else {
				minSizeIndex++
			}
		}
		if minSizeIndex >= len(sizes) {
			break
		}
	}
	return contentCount
}

func main() {
	fmt.Println("1 -> ", findContentChildren([]int{1, 2, 3}, []int{1, 1}))
	fmt.Println("2 -> ", findContentChildren([]int{1, 2}, []int{1, 2, 3}))
}
