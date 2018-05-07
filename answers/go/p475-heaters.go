package main

import "fmt"
import "sort"

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func findRadius(houses []int, heaters []int) int {
	MaxInt := int(^uint(0) >> 1)
	heatersCount := len(heaters)
	calcMinRadius := func(hoursePosition int) int {
		minRadius := MaxInt
		// find the nearest heater position
		index := sort.SearchInts(heaters, hoursePosition)
		// fmt.Println("nearestIndex:", nearestIndex, " heaterPosition: ", nearestHeaterPosition, ", radius:", radius)

		nearestIndex := min(heatersCount-1, index)
		nearestHeaterPosition := heaters[nearestIndex]
		radius := abs(hoursePosition - nearestHeaterPosition)
		if radius < minRadius {
			minRadius = radius
		}

		leftIndex := max(0, index-1)
		leftMinRadius := abs(hoursePosition - heaters[leftIndex])
		if leftMinRadius < minRadius {
			minRadius = leftMinRadius
		}
		rightIndex := min(index+1, heatersCount-1)
		rightMinRadius := abs(heaters[rightIndex] - hoursePosition)
		if rightMinRadius < minRadius {
			minRadius = rightMinRadius
		}
		// fmt.Println("housePosition: ", hoursePosition, " index:", index, " minRadius:", minRadius)
		return minRadius
	}

	sort.Ints(houses)
	sort.Ints(heaters)
	maxRadiu := 0
	for i := 0; i < len(houses); i++ {
		radius := calcMinRadius(houses[i])
		// fmt.Println("house position:", houses[i], " minHeaterRadius:", radius)
		if radius > maxRadiu {
			maxRadiu = radius
		}
	}
	return maxRadiu
}

func main() {
	fmt.Println(" 1 -> ", findRadius([]int{1, 2, 3}, []int{2}))
	fmt.Println(" 1 -> ", findRadius([]int{1, 2, 3, 4}, []int{1, 4}))
	fmt.Println(" 2 -> ", findRadius([]int{1, 2, 3, 4}, []int{2}))
	fmt.Println(" 3 -> ", findRadius([]int{1, 2, 3, 4}, []int{1}))
	fmt.Println(" 2 -> ", findRadius([]int{1, 3}, []int{3}))
	fmt.Println(" 161834419 -> ",
		findRadius([]int{282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923},
			[]int{823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612}))

}
