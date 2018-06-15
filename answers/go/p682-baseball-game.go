package main

import (
	"fmt"
	"strconv"
)

func calPoints(ops []string) int {
	// -1 means canceled
	roundScores := make([]int, len(ops))
	currentRound := -1
	sum := 0
	score := 0
	for i := 0; i < len(ops); i++ {
		op := ops[i]
		currentRound++
		switch op {
		case "C":
			currentRound-- // cancel last round
			prevScore := roundScores[currentRound]
			sum -= prevScore
			roundScores[currentRound] = 0
			currentRound-- // not a round
		case "D":
			score = roundScores[currentRound-1] * 2
			roundScores[currentRound] = score
			sum += score
		case "+":
			score = roundScores[currentRound-1] + roundScores[currentRound-2]
			sum += score
			roundScores[currentRound] = score
		default:
			score, _ = strconv.Atoi(op)
			roundScores[currentRound] = score
			sum += score
		}
		// fmt.Println(op, "\t", score, "\t", sum, "\t", roundScores)
	}
	return sum
}

func main() {
	fmt.Println("30 -> ", calPoints([]string{"5", "2", "C", "D", "+"}))
	fmt.Println("27 -> ", calPoints([]string{"5", "-2", "4", "C", "D", "9", "+", "+"}))
}
