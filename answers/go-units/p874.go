package leetcode

import (
	"fmt"
	"strconv"
)

type direction int

const (
	up    direction = 0
	down            = 1
	left            = 2
	right           = 3
)

func dirToLabel(dir direction) string {
	switch dir {
	case up:
		return "up"
	case down:
		return "down"
	case left:
		return "left"
	case right:
		return "right"
	default:
		return "unkown"
	}
}

func robotSim(commands []int, obstacles [][]int) int {
	x := 0
	y := 0
	dir := up

	packXY := func(x, y int) string {
		return strconv.Itoa(x) + "," + strconv.Itoa(y)
	}
	obstaclesMap := make(map[string]bool)
	for _, obstacle := range obstacles {
		key := packXY(obstacle[0], obstacle[1])
		obstaclesMap[key] = true
	}

	turnLeft := func() {
		switch dir {
		case up:
			dir = left
		case down:
			dir = right
		case left:
			dir = down
		case right:
			dir = up
		}
	}
	turnRight := func() {
		switch dir {
		case up:
			dir = right
		case down:
			dir = left
		case left:
			dir = up
		case right:
			dir = down
		}

	}
	// 返回
	maxPix := 3000001
	findObstaclesInUp := func(y1, y2 int) int {
		for y := y1; y <= y2; y++ {
			key := packXY(x, y)
			if obstaclesMap[key] {
				return y
			}
		}
		return maxPix
	}
	findObstaclesInDown := func(y1, y2 int) int {
		for y := y2; y >= y1; y-- {
			key := packXY(x, y)
			if obstaclesMap[key] {
				return y
			}
		}
		return maxPix
	}

	findObstaclesInRight := func(x1, x2 int) int {
		for x := x1; x <= x2; x++ {
			key := packXY(x, y)
			if obstaclesMap[key] {
				return x
			}
		}
		return maxPix
	}

	findObstaclesInLeft := func(x1, x2 int) int {
		for x := x1; x >= x2; x-- {
			key := packXY(x, y)
			if obstaclesMap[key] {
				return x
			}
		}
		return maxPix
	}

	moveFoward := func(offset int) {
		targetX := x
		targetY := y
		switch dir {
		case up:
			targetY += offset
			adjY := findObstaclesInUp(y, targetY)
			if adjY != maxPix {
				y = adjY - 1
			} else {
				y = targetY
			}
		case down:
			targetY -= offset
			adjY := findObstaclesInDown(y, targetY)
			if adjY != maxPix {
				y = adjY + 1
			} else {
				y = targetY
			}
		case left:
			targetX -= offset
			adjX := findObstaclesInLeft(x, targetX)
			if adjX != maxPix {
				x = adjX + 1
			} else {
				x = targetX
			}
		case right:
			targetX += offset
			adjX := findObstaclesInRight(x, targetX)
			if adjX != maxPix {
				x = adjX - 1
			} else {
				x = targetX
			}
		}
		fmt.Println(dirToLabel(dir), " Command", offset, " -> ", x, y)
	}
	for _, command := range commands {
		switch command {
		case -2:
			turnLeft()
		case -1:
			turnRight()
		default:
			moveFoward(command)
		}
	}
	return x*x + y*y
}
