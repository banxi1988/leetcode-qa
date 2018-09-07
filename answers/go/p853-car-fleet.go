package main

import (
	"fmt"
	"math"
)

func mini(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func carFleet(target int, positions []int, speeds []int) int {
	carCount := len(positions)
	groupCount := 0
	arriveMap := make(map[int]bool)

	// TODO change	 positions to  float64 arr
	fPositions := make([]float64, len(positions))
	fTarget := float64(target)
	for i, pos := range positions {
		fPositions[i] = float64(pos)
	}

	fSpeeds := make([]float64, len(positions))
	for i, sp := range speeds {
		fSpeeds[i] = float64(sp)
	}
	calcFrontestPosition := func() (int, float64) {
		maxPos := -1.0
		index := -1
		for i, pos := range fPositions {
			if pos < fTarget && pos > maxPos {
				maxPos = pos
				index = i
			}
		}
		return index, maxPos
	}
	for {
		group := []int{}
		index, maxPos := calcFrontestPosition()
		// fmt.Println(index, "\t", maxPos)
		// fmt.Println(positions, "\t", speeds)
		maxSpeed := -1.0
		nextMaxPos := -1.0
		duration := 1.0
		if index > -1 {
			// 不能超车，所以需要限速
			maxSpeed = fSpeeds[index]
			nextMaxPos = maxPos + maxSpeed
			// fmt.Println("maxPos=", nextMaxPos, ", maxSpeed=", maxSpeed)
			if nextMaxPos >= fTarget {
				duration = (fTarget - maxPos) / maxSpeed
			}
		}
		for i := 0; i < carCount; i++ {
			pos := fPositions[i]
			if pos >= fTarget {
				arrive, _ := arriveMap[i]
				if arrive {
					continue
				}
				group = append(group, i)
				arriveMap[i] = true
				continue
			} else {
				if index == -1 {
					continue
				}
				speed := fSpeeds[i]
				nextPos := pos + speed*duration
				if nextPos >= fTarget {
					fPositions[i] = nextPos
				} else {
					// 不能超车
					if nextPos >= nextMaxPos {
						fPositions[i] = nextMaxPos
						fSpeeds[i] = math.Min(speed, maxSpeed)
					} else {
						fPositions[i] = nextPos
					}
				}
			}
		}
		// fmt.Println(positions, "\t", speeds)
		if len(group) > 0 {
			// fmt.Println("current group:", group)
			groupCount++
		}

		if len(arriveMap) == carCount {
			break
		}
	}
	return groupCount
}

func main() {
	// fmt.Println("3 -> ", carFleet(12, []int{10, 8, 0, 5, 3}, []int{2, 4, 1, 1, 3}))
	// fmt.Println("1 -> ", carFleet(12, []int{10}, []int{3}))
	// fmt.Println("1 -> ", carFleet(12, []int{10}, []int{2}))
	// fmt.Println("1 -> ", carFleet(12, []int{10}, []int{1}))
	// fmt.Println("1 -> ", carFleet(12, []int{11, 10}, []int{1, 3}))
	// fmt.Println("2 -> ", carFleet(12, []int{10, 10}, []int{2, 1}))
	// fmt.Println("1 -> ", carFleet(10, []int{2, 4}, []int{3, 2}))
	fmt.Println("6 -> ", carFleet(10, []int{3, 4, 5, 6, 7, 8}, []int{4, 4, 4, 4, 4, 4}))
	fmt.Println("2 -> ", carFleet(20, []int{6, 2, 17}, []int{3, 9, 2}))
	// 车辆应该是依次到达，但是上面的计算直接是以 6+4，7 + 4, 8 + 4 这样来计算。 所以算起来 6,7,8 是一起到达的。
	// 但是不是。

}
