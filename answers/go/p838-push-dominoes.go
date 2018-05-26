package main

import (
	"fmt"
)

func pushDominoes(dominoes string) string {
	cards := []byte(dominoes)
	cardCount := len(cards)
	hasChange := true
	for hasChange {
		leftForce := 0
		current := 0
		lastStandIndex := -1
		hasChange = false
		for current < cardCount {
			card := cards[current]
			if lastStandIndex == -1 {
				if card == 'R' {
					leftForce = 1
				} else if card == '.' {
					if leftForce > 0 {
						cards[current] = 'R'
						leftForce = 1 // new force
						hasChange = true
					} else {
						lastStandIndex = current
					}
				} else {
					// 'L' no force
				}
				current++
			} else {
				if card == '.' {
					lastStandIndex = current
				} else if card == 'R' {
					if leftForce > 0 {
						cards[lastStandIndex] = 'R'
						leftForce = 1 // new force
						hasChange = true
					}
					lastStandIndex = -1
				} else {
					// L
					if leftForce > 0 {
						// balance
					} else {
						// fall to left
						cards[lastStandIndex] = 'L'
						hasChange = true
					}
					lastStandIndex = -1
				}
				current++
			}

		}
	}

	return string(cards)
}

func main() {
	// fmt.Println("RR.L ->", pushDominoes("RR.L"))
	fmt.Println("LL.RR.LLRRLL.. ->", pushDominoes(".L.R...LR..L.."))
}
