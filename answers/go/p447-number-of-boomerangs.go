package main

import "fmt"

func distanceOf(point1, point2 []int) int {
	// NOTE: no need to calc square root
	x := point2[0] - point1[0]
	y := point2[1] - point1[1]
	return x*x + y*y
}

func numberOfBoomerangsOfTriangle(point1, point2, point3 []int) int {
	side1 := distanceOf(point1, point2)
	side2 := distanceOf(point2, point3)
	side3 := distanceOf(point3, point1)

	twoSideEqual := side1 == side2 || side1 == side3 || side2 == side3
	threeSideEqual := side1 == side3 && side1 == side2
	if threeSideEqual {
		return 3
	} else if twoSideEqual {
		return 2
	} else {
		return 0
	}
}

func numberOfBoomerangs(points [][]int) int {
	pointsCount := len(points)
	totalCount := 0
	for i := 0; i < (pointsCount - 2); i++ {
		for j := i + 1; j < (pointsCount - 1); j++ {
			for k := j + 1; k < pointsCount; k++ {
				point1 := points[i]
				point2 := points[j]
				point3 := points[k]
				count := numberOfBoomerangsOfTriangle(point1, point2, point3)
				totalCount += count
			}
		}
	}
	return totalCount
}

func main() {
	points1 := [][]int{
		{0, 0},
		{1, 0},
		{2, 0},
	}
	fmt.Println("2 -> ", numberOfBoomerangs(points1))
}
