package leetcode

import (
	"math"
)

func calcTriangleArea(p1, p2, p3 []int) float64 {
	// S=(1/2)*(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2)
	x1 := p1[0]
	y1 := p1[1]
	x2 := p2[0]
	y2 := p2[1]
	x3 := p3[0]
	y3 := p3[1]
	return 0.5 * math.Abs(float64(x1*y2+x2*y3+x3*y1-x1*y3-x2*y1-x3*y2))
}
func largestTriangleArea(points [][]int) float64 {
	pointCount := len(points)
	maxArea := 0.0
	for i := 0; i < pointCount; i++ {
		for j := i + 1; j < pointCount; j++ {
			for k := j + 1; k < pointCount; k++ {
				area := calcTriangleArea(points[i], points[j], points[k])
				if area > maxArea {
					maxArea = area
				}
			}
		}
	}
	return maxArea
}
