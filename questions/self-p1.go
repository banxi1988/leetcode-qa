package main

import "fmt"

const pi = 3.15

func maxRects(radius int) int {

}

func main() {
	radius := 1.5
	for radius < 5 {
		diameter := radius * 2
		perimeter := diameter * pi
		fmt.Println(diameter, perimeter, maxRects(radius))
		radius += 0.1
	}
}
