package main

import "fmt"

func intersection(nums1 []int, nums2 []int) []int {
	map1 := make(map[int]bool)
	map2 := make(map[int]bool)
	for i := 0; i < len(nums1); i++ {
		map1[nums1[i]] = true
	}
	for i := 0; i < len(nums2); i++ {
		map2[nums2[i]] = true
	}
	cnums := []int{}
	for num := range map1 {
		_, ok := map2[num]
		if ok {
			cnums = append(cnums, num)
		}
	}
	return cnums
}

func main() {
	fmt.Println("[2] -> ", intersection([]int{1, 2, 2, 1}, []int{2, 2}))
	fmt.Println("[2,3] -> ", intersection([]int{3, 2, 2, 1}, []int{3, 2}))
}
