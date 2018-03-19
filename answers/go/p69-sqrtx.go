package main

import "fmt"

func mySqrt(x int) int {
	numf := float64(x)
	root := numf
	diff := root*root - numf
	for diff > 0.01 {
		root = root - diff/(2*root)
		diff = root*root - numf
	}
	return int(root)
}

func main() {
	fmt.Println("4 -> 2 ", mySqrt(4))
	fmt.Println("8 -> 2 ", mySqrt(8))
	fmt.Println("9 -> 3 ", mySqrt(9))
	fmt.Println("10 -> 3 ", mySqrt(10))
	fmt.Println("15 -> 3 ", mySqrt(15))
	fmt.Println("16 -> 4 ", mySqrt(10))
}
