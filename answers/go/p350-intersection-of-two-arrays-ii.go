package main

import "fmt"

func intersect(nums1 []int, nums2 []int) []int {
	map1 := make(map[int]int)
	map2 := make(map[int]int)
	for i := 0; i < len(nums1); i++ {
		count, _ := map1[nums1[i]]
		map1[nums1[i]] = count + 1
	}
	for i := 0; i < len(nums2); i++ {
		count, _ := map2[nums2[i]]
		map2[nums2[i]] = count + 1
	}
	cnums := []int{}
	for num, count1 := range map1 {
		count2, _ := map2[num]
		for count := 0; count < count1 && count < count2; count++ {
			cnums = append(cnums, num)
		}
	}
	return cnums
}

func main() {
	fmt.Println("[2,2] -> ", intersect([]int{1, 2, 2, 1}, []int{2, 2}))
	fmt.Println("[2,2] -> ", intersect([]int{1, 2, 2, 1}, []int{3, 2, 3, 2}))
	fmt.Println("[2,3] -> ", intersect([]int{3, 2, 2, 1}, []int{3, 2}))
}
