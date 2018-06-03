package main

import (
	"fmt"
	"sort"
)

func takeOneHand(hand []int, W int) ([]int, bool) {
	prev := hand[0]
	hand = hand[1:]
	handCount := 1
	i := 0
	for handCount < W && i < len(hand) {
		curCard := hand[i]
		if curCard == prev+1 {
			prev = curCard
			handCount++
			hand = append(hand[:i], hand[i+1:]...)
		} else {
			i++
		}
	}

	return hand, handCount == W
}

func isNStraightHand(hand []int, W int) bool {
	if W == 1 {
		return true
	}
	cardCount := len(hand)
	if cardCount%W != 0 {
		return false
	}

	sort.Ints(hand)
	groupCount := cardCount / W
	isStraight := false
	for i := 0; i < groupCount; i++ {
		hand, isStraight = takeOneHand(hand, W)
		if !isStraight {
			// fmt.Println("current hand:", hand)
			// fmt.Println("no ", (i + 1), " straight")
			return false
		}
	}
	return true
}

func main() {
	fmt.Println("true -> ", isNStraightHand([]int{1, 2, 3}, 3))
	// 1,2,3 and 2,3,4 and 6,7,8
	fmt.Println("true -> ", isNStraightHand([]int{1, 2, 3, 6, 2, 3, 4, 7, 8}, 3))
	fmt.Println("false -> ", isNStraightHand([]int{1, 2, 3, 4, 5}, 4))
	fmt.Println("true -> ", isNStraightHand([]int{1, 2, 3, 4, 5}, 1))
	fmt.Println("false -> ", isNStraightHand([]int{1, 2, 3, 4, 5}, 2))
	fmt.Println("false -> ", isNStraightHand([]int{1, 2, 3, 5}, 2))
}
