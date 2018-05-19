package main

import (
	"fmt"
	"sort"
	"strconv"
)

func findRelativeRanks(scores []int) []string {
	scoreCount := len(scores)
	scoreIndexMap := make(map[int]int, scoreCount)
	for i := 0; i < scoreCount; i++ {
		scoreIndexMap[scores[i]] = i
	}
	sort.Sort(sort.Reverse(sort.IntSlice(scores)))
	ranks := make([]string, len(scores))
	for i := 0; i < len(scores); i++ {
		rank := i + 1
		score := scores[i]
		rankIndex, _ := scoreIndexMap[score]
		switch rank {
		case 1:
			ranks[rankIndex] = "Gold Medal"
		case 2:
			ranks[rankIndex] = "Silver Medal"
		case 3:
			ranks[rankIndex] = "Bronze Medal"
		default:
			ranks[rankIndex] = strconv.Itoa(rank)
		}
	}
	return ranks
}

func main() {
	fmt.Println(`["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"] -> `, findRelativeRanks([]int{5, 4, 3, 2, 1}))
	fmt.Println(`["Gold Medal","5","Bronze Medal","Silver Medal","4"] -> `, findRelativeRanks([]int{10, 3, 8, 9, 4}))
}
