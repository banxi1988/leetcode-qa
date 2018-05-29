package main

import (
	"fmt"
)

func findRestaurant(list1 []string, list2 []string) []string {
	likesMap := make(map[string]int)
	for i := 0; i < len(list1); i++ {
		likesMap[list1[i]] = i
	}
	minIndexSum := len(list1) + len(list2)
	minIndexes := []int{}
	for i := 0; i < len(list2); i++ {
		key := list2[i]
		index1, ok := likesMap[key]
		if !ok {
			continue
		}
		indexSum := i + index1
		if indexSum < minIndexSum {
			minIndexSum = indexSum
			minIndexes = []int{index1}
		} else if indexSum == minIndexSum {
			minIndexes = append(minIndexes, index1)
		}
	}
	results := make([]string, len(minIndexes))
	for i, l1Index := range minIndexes {
		results[i] = list1[l1Index]
	}
	return results
}

func main() {
	fmt.Println("Shogun -> ", findRestaurant(
		[]string{"Shogun", "Tapioca Express", "Burger King", "KFC"},
		[]string{"Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"},
	))
	fmt.Println("Shogun -> ", findRestaurant(
		[]string{"Shogun", "Tapioca Express", "Burger King", "KFC"},
		[]string{"KFC", "Shogun", "Burger King"},
	))
}
